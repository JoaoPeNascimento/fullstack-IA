from pydantic import BaseModel
from typing import Optional

class AnalyzeRequest(BaseModel):
    task: str
    input_text: Optional[str]
    use_external: Optional[bool] = False

class AnalyzeResponse(BaseModel):
    id: str
    task: str
    engine: str
    result: dict
    elapsed_time: int
    received_at: str
