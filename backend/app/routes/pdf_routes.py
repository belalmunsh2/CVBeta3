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
    query_params = dict(request.query_params)
    logging.info(f"Paymob callback received with query parameters: {query_params}")
    
    # Extract order_id from query parameters
    order_id_str = request.query_params.get('order')  # Get order_id from query params
    
    if not order_id_str:
        logging.error("Order ID missing in Paymob callback query parameters.")
        error_redirect_url = f"{FRONTEND_BASE_URL.rstrip('/')}/service?error=missing_order_id"  # Redirect with error
        return RedirectResponse(url=error_redirect_url, status_code=302)
    
    # Retrieve download data from temporary_download_urls using order_id as key
    download_data = temporary_download_urls.get(str(order_id_str))  # Use order_id as key
    
    if not download_data:
        logging.error(f"No download data found for order_id: {order_id_str} in temporary_download_urls.")
        error_redirect_url = f"{FRONTEND_BASE_URL.rstrip('/')}/service?error=missing_token"  # Redirect with error
        return RedirectResponse(url=error_redirect_url, status_code=302)
    
    # Extract download_token from the download_data
    download_token = download_data.get("download_token")
    
    if not download_token:
        logging.error(f"No download_token found in download_data for order_id: {order_id_str}")
        error_redirect_url = f"{FRONTEND_BASE_URL.rstrip('/')}/service?error=missing_token"  # Redirect with error
        return RedirectResponse(url=error_redirect_url, status_code=302)
    
    # Construct frontend download URL
    frontend_download_url = f"{FRONTEND_BASE_URL.rstrip('/')}/download/{download_token}"
    
    logging.info(f"Successfully retrieved download_token for order_id: {order_id_str}. Redirecting to frontend download URL: {frontend_download_url}")
    
    return RedirectResponse(url=frontend_download_url, status_code=302)

@router.get("/api/download-cv-pdf/{token}")
async def download_cv_pdf_route(token: str) -> StreamingResponse:
    """
    Endpoint to download the generated CV as a PDF using a temporary token.
    """
    # First, try to find the token directly in temporary_download_urls
    # This handles the case where token is a download_token used as a key (old method)
    if token in temporary_download_urls:
        download_data = temporary_download_urls[token]
        user_text = download_data.get("user_text")
        expiry_timestamp = download_data.get("expiry_timestamp")
        
        if not user_text or not expiry_timestamp:
            raise HTTPException(status_code=400, detail="Invalid download data format.")
            
        if time.time() > expiry_timestamp:
            raise HTTPException(status_code=400, detail="Download link expired.")
            
        # Invalidate token (one-time use)
        del temporary_download_urls[token]
    else:
        # If not found directly, search for the token in download_data values
        # This handles the case where token is a download_token stored in order_id entry (new method)
        found = False
        for order_id, data in list(temporary_download_urls.items()):
            if data.get("download_token") == token:
                user_text = data.get("user_text")
                expiry_timestamp = data.get("expiry_timestamp")
                
                if not user_text or not expiry_timestamp:
                    raise HTTPException(status_code=400, detail="Invalid download data format.")
                    
                if time.time() > expiry_timestamp:
                    raise HTTPException(status_code=400, detail="Download link expired.")
                
                # Invalidate token (one-time use)
                del temporary_download_urls[order_id]
                found = True
                break
                
        if not found:
            raise HTTPException(status_code=400, detail="Invalid download link.")
            
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
