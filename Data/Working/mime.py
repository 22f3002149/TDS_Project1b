# create a python function that take a questiona and context & generate a response using https://api.openai.com/v1 llm 3-small api
import requests

def generate_llm3_small_response(question, context, api_key):
    """
    Generate a response from OpenAI's LLM 3-small model given a question and context.
    Args:
        question (str): The user's question.
        context (str): The context to provide to the model.
        api_key (str): Your OpenAI API key.
    Returns:
        str: The generated response from the model.
    """
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo-0125",  # LLM 3-small (as of 2025, update if needed)
        "messages": [
            {"role": "system", "content": f"Context: {context}"},
            {"role": "user", "content": question}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]