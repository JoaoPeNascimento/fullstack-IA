from fastapi import FastAPI
from app.routes import healthz
from app.routes import analyze

app = FastAPI()

app.include_router(healthz.router)
app.include_router(analyze.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}