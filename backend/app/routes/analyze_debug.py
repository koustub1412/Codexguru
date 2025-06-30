from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel
from datetime import datetime
from bson import ObjectId

from app.auth import get_current_user
from app.services.mistral_7b import summarize_code
from app.services.llama_3_8b import detect_bugs
from app.db import analyses_collection

router = APIRouter()

class CodeInput(BaseModel):
    code: str

class UpdateAnalysis(BaseModel):
    code: str | None = None
    summary: str | None = None
    debug: str | None = None

@router.post("/analyze-debug")
def analyze_and_debug_code(code_input: CodeInput, user: dict = Depends(get_current_user)):
    cached = analyses_collection.find_one({
        "email": user["email"],
        "code": code_input.code
    })
    if cached:
        return {
            "summary": cached.get("summary", ""),
            "debug": cached.get("debug", ""),
            "email": user["email"],
            "cached": True
        }

    summary = summarize_code(code_input.code)
    if not summary:
        raise HTTPException(status_code=502, detail="Failed to summarize code")

    debug_output = detect_bugs(code_input.code)
    if not debug_output:
        raise HTTPException(status_code=502, detail="Failed to debug code")

    analyses_collection.insert_one({
        "email": user["email"],
        "code": code_input.code,
        "summary": summary,
        "debug": debug_output,
        "timestamp": datetime.utcnow()
    })

    return {
        "summary": summary,
        "debug": debug_output,
        "email": user["email"],
        "cached": False
    }

@router.get("/history")
def get_history(user: dict = Depends(get_current_user)):
    history_cursor = analyses_collection.find({"email": user["email"]}).sort("timestamp", -1)
    history = []
    for record in history_cursor:
        history.append({
            "_id": str(record.get("_id")),
            "code": record.get("code", ""),
            "summary": record.get("summary", ""),
            "debug": record.get("debug", ""),
            "timestamp": record.get("timestamp").isoformat() if record.get("timestamp") else ""
        })
    return history

@router.delete("/history/{analysis_id}")
def delete_analysis(analysis_id: str = Path(..., description="ID of the analysis to delete"), user: dict = Depends(get_current_user)):
    result = analyses_collection.delete_one({
        "_id": ObjectId(analysis_id),
        "email": user["email"]
    })
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Analysis not found or unauthorized")
    return {"message": "Analysis deleted successfully"}

@router.put("/history/{analysis_id}")
def update_analysis(analysis_id: str, update: UpdateAnalysis, user: dict = Depends(get_current_user)):
    update_data = {k: v for k, v in update.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No update data provided")

    result = analyses_collection.update_one(
        {"_id": ObjectId(analysis_id), "email": user["email"]},
        {"$set": update_data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Analysis not found or unauthorized")

    return {"message": "Analysis updated successfully"}