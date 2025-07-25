import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

def debug_code(code: str):
    payload = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": f"Debug this code and check for errrors(if any):\n\n{code}"}
        ]
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    print("Status Code:", response.status_code)
    print("Response:", response.text)

# Example
debug_code("def add(a, b):\n return a+b")
