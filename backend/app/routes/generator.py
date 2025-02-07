from fastapi import APIRouter
from app.models.schemas import CVTextInput
from .services.gemini_ai_service import generate_cv_content_gemini

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "OK"}

@router.post("/generate-cv/")
async def generate_cv(cv_text_input: CVTextInput) -> str:
    """
    Endpoint to generate CV content using Gemini AI API.
    """
    user_text = cv_text_input.user_text
    ai_cv_content = generate_cv_content_gemini(user_text)
    return ai_cv_content