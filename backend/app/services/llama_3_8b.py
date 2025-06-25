# app/services/llama_service.py

import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

def detect_bugs(code: str) -> str:
    payload = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": f"check for errors (if any):\n\n{code}"}
        ]
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "LLaMA API failed to debug code."
