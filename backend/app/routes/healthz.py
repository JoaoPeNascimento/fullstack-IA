from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["health check"])

@router.get("/healthz")
def health_check():
    return {"status": "ok"}
