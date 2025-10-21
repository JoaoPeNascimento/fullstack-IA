from fastapi import FastAPI

app = FastAPI()

@app.get("/ap/v1/healtz")
def read_root():
    return {"status": "Ok"}