# santacoder_service.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Global model/tokenizer cache
model = None
tokenizer = None

def load_santacoder():
    global model, tokenizer
    if model is None or tokenizer is None:
        tokenizer = AutoTokenizer.from_pretrained("bigcode/santacoder", trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained("bigcode/santacoder", trust_remote_code=True)
        model.eval()


def summarize_code(code: str) -> str:
    load_santacoder()
    prompt = f"""### Code:
{code}

### Summary:"""
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            max_length=128,
            num_beams=4,
            do_sample=False,
            early_stopping=True,
            pad_token_id=tokenizer.eos_token_id,
        )
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result.split("### Summary:")[-1].strip()
