import time
from transformers import pipeline
from app.core.config import settings

class SummarizeService:
    def __init__(self):
        model_name = settings.MODEL_NAME

        self.summarizer = pipeline("summarization", model=model_name)
    def summarize(self, text: str, max_length: int = 130, min_length: int = 30) -> dict:
        start_time = time.time()

        summary = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )

        elapsed_time = int((time.time() - start_time) * 1000)

        result = {
            "summary_text": summary[0]['summary_text'],
            "elapsed_time_ms": elapsed_time
        }

        return result