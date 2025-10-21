from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/healthz", tags=["health check"])

@router.get("/")
def health_check():
    return {"status": "ok"}
