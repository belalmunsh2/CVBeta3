from fastapi import APIRouter
from app.services.stub_ai import generate_cv_content_stub
from app.models.schemas import CVTextInput

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "OK"}

@router.post("/generate-cv/")
async def generate_cv(cv_text_input: CVTextInput) -> str:
    """
    Endpoint to generate CV content based on user provided text.
    Now expects user_text in the request body as JSON.
    """
    user_text = cv_text_input.user_text
    ai_cv_content = generate_cv_content_stub(user_text)
    return ai_cv_content