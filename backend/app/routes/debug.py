# debug.py

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.auth import get_current_user
from app.services.llama_3_8b import detect_bugs  # This is your DeepSeek function

router = APIRouter()

class CodeInput(BaseModel):
    code: str

@router.post("/debug")
def run_debugger(data: CodeInput, token: str = Depends(get_current_user)):
    output = detect_bugs(data.code)
    return {"output": output}