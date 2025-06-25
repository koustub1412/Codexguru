import os
import requests
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_TOKEN = os.getenv("DEEPSEEK_TOKEN")

def detect_bugs(code: str):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-coder",
        "messages": [
            {"role": "user", "content": f"Find bugs in this code and suggest fixes:\n{code}"}
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "DeepSeek failed to analyze code."
