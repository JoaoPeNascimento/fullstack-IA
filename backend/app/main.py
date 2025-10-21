from fastapi import FastAPI
from app.routes import healthz

app = FastAPI()

app.include_router(healthz.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}