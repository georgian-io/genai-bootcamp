# Readme

## Model Guide

The code in this repository supports and works with the following models:

* OpenAI: `gpt-3.5-turbo`, `gpt-4`
* Google: `chat-bison`, `text-bison` (Chat and Instruction Fine-Tuned versions of PaLM)
* Meta: `Llama-2-7b-chat-hf`, `Llama-2-13b-chat-hf`, `Llama-2-70b-chat-hf`
* Anthropic: `claude-v2`, `claude-instant-v1`

You can make use of any of the models above in the `llm_call` function depicted in the notebooks in this repository, as seen in `03-examples.ipynb`. While this functions exists to facilitate easy swapping between models, when developing a POC you might want to pick one model family and stick to it. In such scenarios, we recommend taking the respective code snippet from either the `tools.py` file or the `01-api-access.ipynb` file. 

We also leave some notes on these models in terms of features they may or may not support (as of October 17 2023).

* Function Calling API: Only OpenAI model support this at this time.
* System Prompt: This is supported out of the box for OpenAI and Meta (hosted via AnyScale) models. Google's text-bison is not a chat model and so does not support it. Google's chat-bison supports this but it is called `context`. Anthropic models technically support it but Claude does not pay a lot of attention to the system prompt, as described [here](https://docs.anthropic.com/claude/docs/constructing-a-prompt#system-prompt-optional).
* Chat History: OpenAI and Meta (hosted via AnyScale) models require a list of messages as input. Prior conversation history can be included here. For the same reason as before, `text-bison` does not support this. `chat-bison` supports this feature and Vertex AI even stores this conversation history in the chat object. Anthropic models do support this but requires the entire conversation in a single string, with human input prepended with a `\n\nHuman:`. In addition, all messages end with a `\n\nAssistant:` for the assistant's response.

## FAQ
This document will contain answers to frequently asked questions. It will be updated regularly, so keep an eye on it.

* What's the difference between a token and a word? Why do people keep saying tokens?

    Tokens can be thought of as alphabets that a model uses. Similar to how we build words using our usual alphabets of A-Z, the model builds words using the tokens it knows. Roughly speaking, 1 token is about 3/4 of a word in English. Most APIs charge you on the basis of token count. For instance, OpenAI's GPT-3.5-Turbo charges $0.0015 per 1K input tokens.

* What does a model's vocabulary refer to?

    A model's vocabulary is simply the total number of tokens that a model knows. 

### Common Terms & Parameters

We are including a short list of common terms and parameters that you might see in our notebooks or elsewhere. 

* `Sampling`: This refers to picking the next word to generate based on some probability distribution. There are a number of different sampling techniques such as `top-k sampling` and `top-p sampling`. `Temperature` is a parameter used in sampling operations. 

* `temperature`: A parameter to control the level of creativity of the model. The higher the temperature, the more likely the model is to output text that is more novel. At the same time, higher values make the model more prone towards hallucination (making things up). A lower value causes the model to try and generate the most probable text instead. Setting the temperature to 0 may be thought of as making the model deterministic (except in the case of GPT-4).

* `top_k`: A parameter that is used to control Top-K Sampling. In essence, when predicting the next word, we usually compute probabilities for the entire vocabulary and then sample from it. In Top-K sampling, we restrict it to only the top-K words and then redistribute the probability mass among them. Ref: https://huggingface.co/blog/how-to-generate#top-k-sampling

* `top_p`: `top_p` is similar to `top_k` sampling but instead of choosing from the `K` most probable words, we instead choose from the smallest set of words whose cumulative probability is higher than some probability `p`. Ref: https://huggingface.co/blog/how-to-generate#top-p-nucleus-sampling

* `max_new_tokens/max_tokens/max_output_tokens`: All of these terms refer to the same parameter, just on different APIs. The terms specify the maximum number of new tokens to be included in the model's output. You can think of this as the maximum number of words you want in your output (not including the input itself).