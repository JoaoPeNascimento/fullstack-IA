from fastapi import FastAPI

app = FastAPI()

@app.post("/ap/v1/analyze")
def read_root():
    return {"message": "Olá, FastAPI!"}