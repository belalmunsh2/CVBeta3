from fastapi import APIRouter
from backend.app.services.stub_ai import generate_cv_content_stub

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "OK"}

@router.post("/generate-cv/")
async def generate_cv(user_text: str) -> str:
    """
    Endpoint to generate CV content based on user provided text.
    For now, using a stubbed AI service.
    """
    ai_cv_content = generate_cv_content_stub(user_text)
    return ai_cv_content