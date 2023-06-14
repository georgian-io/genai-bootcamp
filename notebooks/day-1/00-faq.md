# FAQ

This document will contain answers to frequently asked questions. It will be updated whenever possible, so keep an eye on it!

* What's the difference between a token and a word? Why do people keep saying tokens?

    Tokens can be thought of as alphabets that a model uses. Similar to how we build words using our usual alphabets of A-Z, the model builds words using the tokens it knows. Roughly speaking, 1 token is about 3/4 of a word in English. Most APIs charge you on the basis of token count. For instance, OpenAI's GPT-3.5-Turbo charges $0.0015 per 1K input tokens.

* What does a model's vocabulary refer to?

    A model's vocabulary is simply the total number of tokens that a model knows. 

### Common Terms & Parameters

We are including a short list of common terms nad parameters that you might see in this notebook or elsewhere. 

* `Sampling`: This simply refers to picking the next word to generate based on some probability distribution. There are a number of different sampling techniques such as `top-k sampling` and `top-p sampling`. `Temperature` is a parameter used in sampling operations. 

* `temperature`: A parameter to control the level of creativity of the model. The higher this is, the more likely the model is to output text that is more novel. At the same time, higher values do make the model more prone towards hallucination (making things up). 

* `top_k`: A parameter that is used to control Top-K Sampling. In essence, when predicting the next word, we usually compute probabilities for the entire vocabulary and then sample from it. In Top-K sampling, we restrict it to only the top-K words and then redistribute the probability mass among them. Ref: https://huggingface.co/blog/how-to-generate#top-k-sampling

* `top_p`: This is similar to `top_k` sampling but instead of choosing from the `K` most probable words, we instead choose from the smallest set of words whose cumulative probability is higher than some probability `p`. Ref: https://huggingface.co/blog/how-to-generate#top-p-nucleus-sampling

* `max_new_tokens/max_tokens/max_output_tokens`: All of these refer to the same parameter, just on different APIs. It specifies the maximum number of new tokens to be included in the model's output. You can think of this as the maximum number of words you want in your output (not including the input itself).


---

# classifcation

## Chain of Thought
- Add a prompt that forces the model to "think" about why something would be classified as positive or negative first before making a final classification
- Bonus: Find an example where original answer is wrong and CoT fixes it

# Summarization
## Prompt Chaining

for chunk in get_chunks(document)
    summaries.append(summarize(chunk))

summary = summarize('\n'.join(summaries))

## Private
summarize(strip_private(document))

# entity extraction
## Memory + Search

- Explain embeddings
- Add Vector DB Search
- Replicate example above even when adding a bunch of irrelevant content

# code generation
## python agent
https://python.langchain.com/en/latest/modules/agents/toolkits/examples/python.html
