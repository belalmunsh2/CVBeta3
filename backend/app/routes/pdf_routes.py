from fastapi import APIRouter, Response, HTTPException, Request
from fastapi.responses import StreamingResponse, PlainTextResponse, RedirectResponse
from typing import Optional, Dict, Any
import logging
import uuid
import time
import os
from app.models.schemas import CVTextInput
from ..services.gemini_ai_service import generate_cv_content_gemini
from ..services.pdf_service import convert_html_to_pdf, generate_cv_html
from ..config import PUBLIC_BASE_URL
import io

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

# Dictionary to store temporary download URLs with their expiry timestamps
temporary_download_urls: Dict[str, Dict[str, Any]] = {}

# Frontend base URL - Replace with your actual frontend URL
FRONTEND_BASE_URL = "https://cuddly-engine-pjwvppv46rqgf7q7j-5173.app.github.dev"

@router.post("/api/get-download-url/")
async def get_download_url_route(cv_text_input: CVTextInput, request: Request) -> Dict[str, str]:
    """
    Endpoint to generate a temporary download URL for the CV PDF using frontend URL.
    """
    user_text = cv_text_input.user_text

    download_token = str(uuid.uuid4())
    
    # Construct a frontend URL for the download page
    temporary_url = f"{FRONTEND_BASE_URL.rstrip('/')}/download/{download_token}"
    
    logging.info(f"Generated temporary download URL: {temporary_url}")

    temporary_download_urls[download_token] = {
        "user_text": user_text,
        "expiry_timestamp": time.time() + 300  # 5 minutes expiry
    }

    return {"download_url": temporary_url}

@router.get("/api/paymob-callback-intermediate")
async def paymob_callback_intermediate_route(request: Request):
    """
    Intermediate callback route for Paymob to redirect to after successful payment.
    This route will redirect the user to the frontend download page, passing the download token.
    """
    # **IMPORTANT: Token Retrieval - This is a placeholder!**
    # **We need to figure out how to securely retrieve the correct download_token here.**
    # **For now, let's *assume* we can somehow identify and retrieve the correct token.**
    # **This is the CRITICAL part to solve next!**
    download_token = "DUMMY_TOKEN_FOR_NOW"  # <--- Placeholder - Replace this with actual token retrieval logic!

    # **IMPORTANT: Replace with your *actual* frontend base URL if different!**
    frontend_download_url = f"{FRONTEND_BASE_URL.rstrip('/')}/download/{download_token}"

    logging.info(f"Paymob callback received. Redirecting to frontend download URL: {frontend_download_url}")

    return RedirectResponse(url=frontend_download_url, status_code=302)  # 302 Found is a common redirect status

@router.get("/api/download-cv-pdf/{token}")
async def download_cv_pdf_route(token: str) -> StreamingResponse:
    """
    Endpoint to download the generated CV as a PDF using a temporary token.
    """
    if token not in temporary_download_urls:
        raise HTTPException(status_code=400, detail="Invalid download link.")

    download_data = temporary_download_urls[token]
    expiry_timestamp = download_data["expiry_timestamp"]
    if time.time() > expiry_timestamp:
        raise HTTPException(status_code=400, detail="Download link expired.")

    user_text = download_data["user_text"]

    del temporary_download_urls[token]  # Invalidate token (one-time use)

    ai_cv_content = generate_cv_content_gemini(user_text)  # Re-generate AI content
    html_content = generate_cv_html(ai_cv_content)
    pdf_bytes = convert_html_to_pdf(html_content)

    if pdf_bytes:
        return StreamingResponse(
            io.BytesIO(pdf_bytes),
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment;filename=cv.pdf"}
        )
    else:
        raise HTTPException(status_code=500, detail="PDF generation failed")

@router.post("/api/download-cv-pdf/")
async def download_cv_pdf_direct_route(cv_text_input: CVTextInput) -> StreamingResponse:
    """
    Endpoint to download the generated CV as a PDF.
    This is the original direct download route, kept for backward compatibility.
    """
    user_text = cv_text_input.user_text
    ai_cv_content = generate_cv_content_gemini(user_text)  # Re-generate AI content
    html_content = generate_cv_html(ai_cv_content)  # Use generate_cv_html from pdf_service.py
    pdf_bytes = convert_html_to_pdf(html_content)  # Use convert_html_to_pdf from pdf_service.py

    if pdf_bytes:
        return StreamingResponse(
            io.BytesIO(pdf_bytes),
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment;filename=cv.pdf"}
        )
    else:
        raise HTTPException(status_code=500, detail="PDF generation failed")
