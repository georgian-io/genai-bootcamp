#!/bin/bash
​
​
# Use the financial dataset (sentiment classification) 
# with LoRA and Flan-T5-Large
python seq2seq.py --dataset financial --peft_method lora --r 4 --dropout_rate 0.1 --pretrained_ckpt google/flan-t5-large > lora_flan_financial_metrics.csv

# Use the samsum dataset (summarization)
# with Prefix tuning and Flan-T5-large
python seq2seq.py --dataset samsum --peft_method prefix --prefix_size 50 --prefix_projection --pretrained_ckpt google/flan-t5-large > prefix_flan_samsum_metrics.csv