# app/services/llama_3_8b.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def detect_bugs(code: str) -> str:
    if not OPENROUTER_API_KEY:
        return "❌ Missing OpenRouter API key."

    prompt = f"""Debug the code and point out the errors(if any) limit to 75 words```python{code}```"""
    payload = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300,
        "temperature": 0.3
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        else:
            return f"❌ API Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"