from fastapi import APIRouter, Response, HTTPException, StreamingResponse
from fastapi.responses import PlainTextResponse
from typing import Optional
import logging
from app.models.schemas import CVTextInput
from ..services.gemini_ai_service import generate_cv_content_gemini
from ..services.pdf_service import convert_html_to_pdf, generate_cv_html
import io

# Configure logging
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/api/download-cv-pdf/")
async def download_cv_pdf_route(cv_text_input: CVTextInput) -> StreamingResponse:
    """
    Endpoint to download the generated CV as a PDF.
    """
    user_text = cv_text_input.user_text
    ai_cv_content = generate_cv_content_gemini(user_text) # Re-generate AI content
    html_content = generate_cv_html(ai_cv_content) # Use generate_cv_html from pdf_service.py
    pdf_bytes = convert_html_to_pdf(html_content) # Use convert_html_to_pdf from pdf_service.py

    if pdf_bytes:
        return StreamingResponse(
            io.BytesIO(pdf_bytes),
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment;filename=cv.pdf"}
        )
    else:
        raise HTTPException(status_code=500, detail="PDF generation failed")
