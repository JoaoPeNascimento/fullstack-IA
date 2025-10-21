import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseModel):
    MODEL_NAME: str = os.getenv("MODEL_NAME", "facebook/bart-large-cnn")
    USE_EXTERNAL: bool = os.getenv("USE_EXTERNAL", "False").lower() in ("true", "1", "yes")

settings = Settings()