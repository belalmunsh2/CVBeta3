from fastapi import APIRouter, Response, HTTPException
from fastapi.responses import PlainTextResponse
from typing import Optional
import logging
from app.models.schemas import CVTextInput
from ..services.gemini_ai_service import generate_cv_content_gemini

# Configure logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/generate-cv/")
async def generate_cv(cv_text_input: CVTextInput) -> PlainTextResponse:
    """
    Endpoint to generate CV content using the Gemini AI model.
    """
    user_text = cv_text_input.user_text
    ai_cv_content = generate_cv_content_gemini(user_text)
    print("Backend: /generate-cv/ - AI generated content (plain text, no PDF):")
    print(ai_cv_content)
    return PlainTextResponse(content=ai_cv_content)