# app/services/mistral_7b.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # Add this to .env file

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost:3000",  # required
    "X-Title": "CodexGuru"  # required
}


def summarize_code(code: str) -> str:
    if not OPENROUTER_API_KEY:
        return "❌ API key is missing. Please set OPENROUTER_API_KEY in your .env."

    prompt = f"Summarize this code:\n```python\n{code}\n```"
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150,
        "temperature": 0.3
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)

        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            print(f"❌ Request failed with {response.status_code}: {response.text}")
            return "Summarization failed."

    except Exception as e:
        print("❌ Exception during OpenRouter API call:", str(e))
        return "Summarization failed."