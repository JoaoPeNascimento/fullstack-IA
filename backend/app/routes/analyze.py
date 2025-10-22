from datetime import datetime, timezone
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from app.core.config import settings

from app.models.schemas import AnalyzeRequest, AnalyzeResponse
from app.services.ai_service import SummarizeService


router = APIRouter(prefix="/api/v1", tags=["analyze"])

summarizer = SummarizeService()

@router.post("/analyze", response_model= AnalyzeResponse)
def analyze_text(request: AnalyzeRequest):

    if not request.input_text:
        raise HTTPException(status_code=400, detail="input_text é obrigatório.")
    
    if request.task.lower() != "summarize":
        raise HTTPException(status_code=400, detail="task inválida. Use 'summarize'.")
    
    result = summarizer.summarize(request.input_text)

    response = AnalyzeResponse(
        id=str(uuid4()),
        task="summarize",
        engine=f"local:{settings.MODEL_NAME}",
        result={"summary_text": result["summary_text"]},
        elapsed_time=result["elapsed_time"],
        received_at=datetime.now(timezone.utc).isoformat()
    )   

    return response
