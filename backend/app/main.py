from fastapi import FastAPI
from app.routes import healthz
from app.routes import analyze
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  # porta do Vite
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(healthz.router)
app.include_router(analyze.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}