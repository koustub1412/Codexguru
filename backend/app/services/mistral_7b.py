import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": "Bearer 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",  # Replace with your OpenRouter key
    "Content-Type": "application/json"
}

def summarize_code(code: str) -> str:
    prompt = f"Summarize this code:\n```python\n{code}\n```"
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150,
        "temperature": 0.3
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return "Summarization failed."
