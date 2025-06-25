from fastapi import APIRouter, Depends, HTTPException
from app.auth import get_current_user
from pydantic import BaseModel
from datetime import datetime
from app.db import analyses_collection
from app.services.starcoder_service import summarize_code
from app.services.deepseek_service import detect_bugs
from app.services.starcoder_service import summarize_code


router = APIRouter()

class CodeInput(BaseModel):
    code: str

@router.post("/analyze")
def analyze_code(data: CodeInput, token: str = Depends(get_current_user)):
    code = data.code
    summary = summarize_code(code)
    return {
        "summary": summary,
        "errors": []  # we’ll add DeepSeek later
    }
