# app/routes/analyze.py

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.auth import get_current_user
from app.services.mistral_7b import summarize_code

router = APIRouter()

class CodeInput(BaseModel):
    code: str

@router.post("/analyze")
def analyze_code(code_input: CodeInput, user: dict = Depends(get_current_user)):
    summary = summarize_code(code_input.code)
    return {"summary": summary}
