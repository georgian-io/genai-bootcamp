import openai
from vertexai.preview.language_models import TextGenerationModel, ChatModel
from typing import List, Dict, Any, Tuple, Optional

text_bison = TextGenerationModel.from_pretrained("text-bison@001")
chat_bison = ChatModel.from_pretrained("chat-bison@001")

def parameter_handler(parameters: Dict[str, Any], model: str) -> Dict[str, Any]:
    """
    This function handles the most common parameters used namely:
        temperature (no change b/w models)
        top_p (no change b/w models)
        top_k (not present in openai; exists for google)
        max_tokens (changes between models)
    """
    new_parameters = {}
    for parameter, value in parameters.items():
        if parameter in ["max_tokens", "max_output_tokens", "n_tokens"]:
            if model in ["gpt-3.5-turbo", "gpt-4"]:
                new_parameters["max_tokens"] = value
            elif model in ["chat-bison", "text-bison"]:
                new_parameters["max_output_tokens"] = value
        else:
            new_parameters[parameter] = value
    return new_parameters

def llm_call(
        model: str, 
        prompt: str, 
        parameters: Dict[str, Any]={}, 
        system_prompt: str="", 
        chat_history: List=[],
        return_chat_history=False,
    ) -> Tuple[str, Optional[List]]:
    # Rename parameters for specific models
    parameters = parameter_handler(parameters, model)
    # Run inference based on model
    if model in ["gpt-3.5-turbo", "gpt-4"]:
        if chat_history:
            chat_history.append({"role": "user", "content": prompt})
        else:
            chat_history = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        response = openai.ChatCompletion.create(
            model=model,
            messages=chat_history,
            **parameters
        )
        result = response.choices[0].message["content"]
        chat_history.append({"role": "assistant", "content": result})
    elif model == "chat-bison":
        chat = chat_bison.start_chat(context=system_prompt, message_history=chat_history)
        response = chat.send_message(prompt, **parameters)
        result = response.text
        chat_history = chat.message_history
    elif model == "text-bison":
        # Text bison does not support system prompts or chat history
        response = text_bison.predict(prompt, **parameters)
        result = response.text
        chat_history = []

    if return_chat_history:
        return result, chat_history
    return result