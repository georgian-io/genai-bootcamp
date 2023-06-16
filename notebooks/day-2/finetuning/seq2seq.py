from transformers import (
    AutoModelForSeq2SeqLM, 
    AutoModelForCausalLM, 
    Trainer, 
    TrainingArguments, 
    AdamW, 
    get_linear_schedule_with_warmup,
    AutoModel
    )
from peft import (
    get_peft_config, 
    get_peft_model, 
    get_peft_model_state_dict, 
    TaskType, 
    LoraConfig,
    PrefixTuningConfig, 
    PromptTuningConfig, 
    PromptEncoderConfig,
    PromptTuningInit, 
)
import argparse
import functools
import torch
from datasets import load_dataset
import os
import numpy as np
import evaluate

from transformers import AutoTokenizer
from torch.utils.data import DataLoader
from transformers import default_data_collator, get_linear_schedule_with_warmup
from tqdm import tqdm
from datasets import load_dataset, load_metric
import csv


CLASSIFICATION_DATASETS = ["financial"]
SUMMARIZATION_DATASETS = ["samsum"]

def preprocess_function(examples, tokenizer, text_column, label_column, max_length, args):


    inputs = [text.replace('\n', ' ') for text in examples[text_column]]

    model_inputs = tokenizer(inputs, max_length=max_length, padding="max_length", truncation=True, return_tensors="pt")


    if args.dataset in CLASSIFICATION_DATASETS:
        targets = examples["text_label"]
        labels = tokenizer(targets, max_length=2, padding="max_length", truncation=True, return_tensors="pt")
        labels = labels["input_ids"]
        labels[labels == tokenizer.pad_token_id] = -100
        model_inputs["labels"] = labels

    elif args.dataset in SUMMARIZATION_DATASETS:
        targets = examples[label_column]

        labels = tokenizer(targets, max_length=max_length, padding="max_length", truncation=True, return_tensors="pt")

        model_inputs["labels"] = labels["input_ids"]

    return model_inputs


def main(args):
    print(args)
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    device = "cuda"

    model_name_or_path = args.pretrained_ckpt

    max_length = 128

    lr = 3e-4
    num_epochs = 3

    if args.n_train_data and args.n_train_data <= 100:
        num_epochs = 10
        

    batch_size = 8

    grad_accumulation_steps = 1


    # loading dataset
    if args.dataset == "financial":
        dataset = load_dataset("financial_phrasebank", "sentences_allagree")
        text_column = "sentence"
        label_column = "label"
        label_max_length = 2
        prompt_init_text = "Classify if the text sentiment is negative, neutral or positive:"
        
    
    elif args.dataset == "samsum":
        dataset = load_dataset("samsum")
        text_column = "dialogue"
        label_column = "summary"
        prompt_init_text = "Summarize this text:"


    
    if args.peft_method == "lora":
        peft_config = LoraConfig(
            task_type=TaskType.CAUSAL_LM, inference_mode=False, r=args.r, lora_alpha=32, lora_dropout=args.dropout_rate
        )
        
    elif args.peft_method == "prefix":
        peft_config = PrefixTuningConfig(task_type=TaskType.CAUSAL_LM, 
                                         inference_mode=False, 
                                         num_virtual_tokens=args.prefix_size, 
                                         prefix_projection=args.prefix_projection
                                         )
    elif args.peft_method == "prompt":
        peft_config = PromptTuningConfig(task_type=TaskType.CAUSAL_LM, 
                                         inference_mode=False, 
                                         num_virtual_tokens=args.prefix_size,
                                         prompt_tuning_init=PromptTuningInit.TEXT if args.prompt_init == "text" else PromptTuningInit.RANDOM,
                                         prompt_tuning_init_text=prompt_init_text,
                                         tokenizer_name_or_path=args.pretrained_ckpt)
                                         
    elif args.peft_method == "p_tuning":
        peft_config = PromptEncoderConfig(
            task_type=TaskType.CAUSAL_LM, 
            inference_mode=False, 
            num_virtual_tokens=args.prefix_size, 
            encoder_hidden_size=128,
            encoder_reparameterization_type="MLP")


    model = AutoModelForSeq2SeqLM.from_pretrained(model_name_or_path)
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    dataset = dataset["train"].train_test_split(test_size=200, seed=42, shuffle=True)
    dataset["validation"] = dataset["test"]
    
    
    if args.n_train_data:
        dataset["train"] = dataset["train"].shuffle(seed=42).select(range(args.n_train_data))

    del dataset["test"]

    if args.dataset in CLASSIFICATION_DATASETS:
        classes = dataset["train"].features[label_column].names
        dataset = dataset.map(
            lambda x: {"text_label": [classes[label] for label in x[label_column]]},
            batched=True,
            num_proc=1,
        )

    # data preprocessing
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)


    processed_datasets = dataset.map(
        functools.partial(preprocess_function, tokenizer=tokenizer, text_column=text_column, label_column=label_column, max_length=max_length, args=args),
        batched=True,
        num_proc=1,
        remove_columns=dataset["train"].column_names,
        load_from_cache_file=False,
        desc="Running tokenizer on dataset",
    )

    train_dataset = processed_datasets["train"]
    eval_dataset = processed_datasets["validation"]

    train_dataloader = DataLoader(
        train_dataset, shuffle=True, collate_fn=default_data_collator, batch_size=batch_size, pin_memory=True
    )
    eval_dataloader = DataLoader(eval_dataset, collate_fn=default_data_collator, batch_size=8, pin_memory=True)


    # Define the optimizer and learning rate scheduler
    optimizer = AdamW(model.parameters(), lr=lr)


    # training and evaluation
    model = model.to(device)

    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        for step, batch in enumerate(tqdm(train_dataloader)):

            
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            loss = outputs.loss
            total_loss += loss.detach().float()
            loss.backward()
            

            if (step % grad_accumulation_steps == 0) or step == len(train_dataloader):
                optimizer.step()
                optimizer.zero_grad()
            

        model.eval()
        eval_loss = 0
        eval_preds = []
        for step, batch in enumerate(tqdm(eval_dataloader)):
            batch = {k: v.to(device) for k, v in batch.items()}
            with torch.no_grad():
                outputs = model(**batch)

            loss = outputs.loss
            eval_loss += loss.detach().float()
            

            if args.dataset in CLASSIFICATION_DATASETS:
                preds = tokenizer.batch_decode(torch.argmax(outputs.logits, -1).detach().cpu().numpy(), skip_special_tokens=True)
                
            elif args.dataset in SUMMARIZATION_DATASETS:
                
                with torch.no_grad():
                    preds = tokenizer.batch_decode(
                        model.generate(input_ids=batch["input_ids"], max_new_tokens=1024, do_sample=True, top_p=0.9), 
                        skip_special_tokens=True

                    )

            eval_preds.extend(preds)
        eval_epoch_loss = eval_loss / len(eval_dataloader)
        eval_ppl = torch.exp(eval_epoch_loss)
        train_epoch_loss = total_loss / len(train_dataloader)
        train_ppl = torch.exp(train_epoch_loss)
        print(f"{epoch=}: {train_ppl=} {train_epoch_loss=} {eval_ppl=} {eval_epoch_loss=}")


    if args.dataset in CLASSIFICATION_DATASETS:
        # print accuracy
        correct = 0
        total = 0
        for pred, true in zip(eval_preds, dataset["validation"]["text_label"]):
            if pred.strip() == true.strip():
                correct += 1
            total += 1
        accuracy = correct / total * 100
        print(f"{accuracy=} % on the evaluation dataset")
        print(f"{eval_preds[40:60]=}")
        print(f"{dataset['validation']['text_label'][40:60]=}")


    elif args.dataset in SUMMARIZATION_DATASETS:

        total_rouge1 = 0
        total_rouge2 = 0
        total_rougeL = 0
        total = 0
        rouge_metric = evaluate.load("rouge")
        rouge_dict = rouge_metric.compute(predictions=eval_preds, references=dataset["validation"][label_column])        

        print(f"{rouge_dict['rouge1']=} on the evaluation dataset")
        print(f"{rouge_dict['rouge2']=} on the evaluation dataset")
        print(f"{rouge_dict['rougeL']=} on the evaluation dataset")
        
        print(f"{dataset['validation'][text_column][:2]=}")
        print(f"{dataset['validation'][label_column][:2]=}")
        print(f"{eval_preds[:2]=}")
        


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--pretrained_ckpt", default="google/flan-t5-large", help="Huggingface model name")
    parser.add_argument("--peft_method", default="lora", help="PEFT method from {lora, prefix, prompt, p_tuning}")
    parser.add_argument("--dataset", default="financial", help="dataset from {financial, samsum}")
    parser.add_argument("--n_train_data", default=None, type=int, help="number of training examples to use")
    parser.add_argument("--prefix_size", default=20, type=int, help="prefix length for prefix and prompt tuning")
    parser.add_argument("--r", default=4, type=int, help="r parameter fo LoRA")
    parser.add_argument("--dropout_rate", default=0.1, type=float, help="dropout rate")
    parser.add_argument("--prefix_projection", action="store_true", help="whether to have an MLP project embedings for prefix tuning")
    parser.add_argument("--prompt_init", default="random", help="how to initialize prompts from {random, text}")
    parser.add_argument("--exp_name", default="test_preds.csv", help="experiment name")



    args = parser.parse_args()
    main(args)
