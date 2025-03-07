from fastapi import APIRouter, Response, HTTPException, Request
from fastapi.responses import StreamingResponse, PlainTextResponse, RedirectResponse
from starlette.responses import FileResponse
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
import hashlib

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
async def download_cv_pdf_route(token: str, request: Request, response_class=StreamingResponse):
    """
    Endpoint to download the generated CV as a PDF.
    This is the streamed download route for pre-generated CVs.
    """
    logging.info(f"ENTRY: download_cv_pdf_route called with token: {token[:8]}...")
    
    # First check if the token exists directly
    user_text = None
    if token in temporary_download_urls:
        logging.info(f"Token {token[:8]}... found directly in temporary_download_urls")
        user_text = temporary_download_urls[token]["user_text"]
    else:
        # Look for token in order entries
        logging.info(f"Token {token[:8]}... not found directly, searching in order entries")
        found = False
        for order_id, data in temporary_download_urls.items():
            if isinstance(data, dict) and data.get("download_token") == token:
                user_text = data.get("user_text")
                token = data.get("download_token")
                logging.info(f"Found token {token[:8]}... via order_id {order_id}")
                found = True
                break
                
        if not found:
            logging.error(f"Token {token[:8]}... not found in any temporary_download_urls entries. Current entries: {list(temporary_download_urls.keys())}")
            raise HTTPException(status_code=400, detail="Invalid download link.")
    
    # *** ENHANCED LOGGING - User text retrieved ***
    logging.info(f"Retrieved user_text for token {token[:8]}...: {user_text[:50]}..." if user_text else "No user_text found")
    
    try:
        # *** ENHANCED ERROR HANDLING - Try...except block for PDF generation ***
        logging.info(f"Before generate_cv_content_gemini call for token {token[:8]}...")
        ai_cv_content = generate_cv_content_gemini(user_text)  # Re-generate AI content
        logging.info(f"After generate_cv_content_gemini: content length = {len(ai_cv_content) if ai_cv_content else 'None'}")
        
        logging.info(f"Before generate_cv_html call for token {token[:8]}...")
        html_content = generate_cv_html(ai_cv_content)
        logging.info(f"After generate_cv_html: HTML content length = {len(html_content) if html_content else 'None'}")
        
        logging.info(f"Before convert_html_to_pdf call for token {token[:8]}...")
        pdf_bytes = convert_html_to_pdf(html_content)
        if pdf_bytes is None:
            logging.error(f"convert_html_to_pdf returned None!")
        else:
            logging.info(f"After convert_html_to_pdf: PDF size = {len(pdf_bytes)} bytes")
        
        if pdf_bytes:
            logging.info(f"Before creating StreamingResponse: PDF size = {len(pdf_bytes)} bytes")

            # --- START: Temporary SAVE PDF TO DISK for debugging ---
            try:
                filepath = f"/tmp/cv_download_{token[:8]}.pdf" # Choose /tmp directory for saving
                with open(filepath, 'wb') as f:
                    f.write(pdf_bytes)
                logging.info(f"Saved PDF to disk for debugging: {filepath}") # Log the saved filepath
            except Exception as e:
                logging.error(f"Error saving PDF to disk: {e}")
            # --- END: Temporary SAVE PDF TO DISK for debugging ---
            
            return StreamingResponse(
                io.BytesIO(pdf_bytes),
                media_type="application/pdf",
                headers={"Content-Disposition": f"attachment;filename=cv_{token[:8]}.pdf"}
            )
        else:
            logging.error(f"PDF generation failed - pdf_bytes is None!")
            raise HTTPException(status_code=500, detail="PDF generation failed - no bytes returned")
    except Exception as e:
        # *** ENHANCED ERROR HANDLING - Catch any exception during PDF generation ***
        logging.exception(f"Error generating PDF for token {token[:8]}...: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating PDF: {str(e)}")

@router.get("/api/download-cv-pdf-file/{token}")
async def download_cv_pdf_file_route(token: str, request: Request):
    """
    TEST ENDPOINT: Alternative implementation that saves PDF to file and serves it directly.
    This bypasses StreamingResponse to determine if that's causing the corruption.
    """
    # First check if the token exists and is valid
    if token not in temporary_download_urls:
        for order_id, data in temporary_download_urls.items():
            if isinstance(data, dict) and data.get("download_token") == token:
                user_text = data.get("user_text")
                token = data.get("download_token")
                logging.info(f"Found token {token} via order_id {order_id}")
                break
        else:
            raise HTTPException(status_code=400, detail="Invalid download link.")
    else:
        # Get the user_text from the token
        user_text = temporary_download_urls[token]["user_text"]
    
    logging.info(f"Starting PDF generation via FILE serving route for token {token}")
    
    try:
        ai_cv_content = generate_cv_content_gemini(user_text)
        logging.info(f"AI content generated for file serving route")
        
        html_content = generate_cv_html(ai_cv_content)
        logging.info(f"HTML content generated for file serving route")
        
        pdf_bytes = convert_html_to_pdf(html_content)
        
        if not pdf_bytes or len(pdf_bytes) < 100:
            logging.error(f"Generated PDF seems invalid, size: {len(pdf_bytes) if pdf_bytes else 0} bytes")
            raise HTTPException(status_code=500, detail="Generated PDF file appears invalid")
        
        # Save to a temporary file with unique name
        temp_filename = f"cv_download_{token[:8]}_{int(time.time())}.pdf"
        file_path = f"/tmp/{temp_filename}"
        
        with open(file_path, "wb") as f:
            f.write(pdf_bytes)
        
        logging.info(f"Saved PDF to {file_path}, size: {len(pdf_bytes)} bytes")
        
        # Return a FileResponse instead of StreamingResponse
        return FileResponse(
            path=file_path,
            filename=f"cv_{token[:8]}.pdf",
            media_type="application/pdf"
        )
    except Exception as e:
        logging.exception(f"Error in file-based PDF download: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating PDF: {str(e)}")

@router.get("/api/download-cv-pdf-debug/{token}")
async def download_cv_pdf_debug_route(token: str, request: Request):
    """
    TEST ENDPOINT: Modified streaming implementation with enhanced debugging
    and explicit headers to diagnose PDF streaming issues.
    """
    # Token validation (same as the original endpoint)
    if token not in temporary_download_urls:
        for order_id, data in temporary_download_urls.items():
            if isinstance(data, dict) and data.get("download_token") == token:
                user_text = data.get("user_text")
                token = data.get("download_token")
                logging.info(f"Found token {token} via order_id {order_id}")
                break
        else:
            raise HTTPException(status_code=400, detail="Invalid download link.")
    else:
        user_text = temporary_download_urls[token]["user_text"]
    
    logging.info(f"Starting PDF generation via DEBUG streaming route for token {token}")
    
    try:
        ai_cv_content = generate_cv_content_gemini(user_text)
        logging.info(f"AI content generated for debug route")
        
        html_content = generate_cv_html(ai_cv_content)
        logging.info(f"HTML content generated for debug route")
        
        pdf_bytes = convert_html_to_pdf(html_content)
        logging.info(f"PDF conversion completed, size: {len(pdf_bytes) if pdf_bytes else 'None'} bytes")
        
        if not pdf_bytes or len(pdf_bytes) < 100:
            logging.error(f"Generated PDF seems invalid, size: {len(pdf_bytes) if pdf_bytes else 0} bytes")
            raise HTTPException(status_code=500, detail="Generated PDF file appears invalid")
        
        # Save PDF to file for comparison
        debug_filename = f"cv_debug_{token[:8]}_{int(time.time())}.pdf"
        debug_path = f"/tmp/{debug_filename}"
        
        with open(debug_path, "wb") as f:
            f.write(pdf_bytes)
        
        logging.info(f"Saved debug PDF to {debug_path}, size: {len(pdf_bytes)} bytes")
        
        # Calculate MD5 hash of the PDF bytes for debugging
        pdf_hash = hashlib.md5(pdf_bytes).hexdigest()
        logging.info(f"PDF MD5 hash before streaming: {pdf_hash}")
        
        # Create a fresh BytesIO object from the by tes  
        pdf_stream = io.BytesIO(pdf_bytes)
        
        # Set explicit and comprehensive headers
        headers = {
            "Content-Disposition": f"attachment; filename=\"cv_{token[:8]}.pdf\"",
            "Content-Type": "application/pdf",
            "Content-Length": str(len(pdf_bytes)),
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0"
        }
        
        # Use a direct Response instead of StreamingResponse for testing
        # return Response(content=pdf_bytes, media_type="application/pdf", headers=headers)
        
        # Or use StreamingResponse with explicit chunk size
        return StreamingResponse(
            pdf_stream,
            media_type="application/pdf",
            headers=headers
        )
    except Exception as e:
        logging.exception(f"Error in debug PDF download: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating PDF: {str(e)}")

@router.get("/api/download-cv-pdf-direct/{token}")
async def download_cv_pdf_direct_debug(token: str, request: Request):
    """
    Simplified debug endpoint that directly returns the PDF without complex streaming.
    This minimal implementation helps isolate potential issues in StreamingResponse.
    """
    # Token validation (simplified from main route)
    if token not in temporary_download_urls:
        for order_id, data in temporary_download_urls.items():
            if isinstance(data, dict) and data.get("download_token") == token:
                user_text = data.get("user_text")
                token = data.get("download_token")
                break
        else:
            raise HTTPException(status_code=400, detail="Invalid download token")
    else:
        user_text = temporary_download_urls[token]["user_text"]
    
    # Generate PDF with minimal steps
    logging.info(f"Starting simplified PDF generation for token {token}")
    ai_cv_content = generate_cv_content_gemini(user_text)  
    html_content = generate_cv_html(ai_cv_content)
    pdf_bytes = convert_html_to_pdf(html_content)
    
    if not pdf_bytes:
        logging.error("PDF generation failed - empty or None bytes returned")
        raise HTTPException(status_code=500, detail="PDF generation failed")
    
    # Log basic info
    logging.info(f"Generated PDF size: {len(pdf_bytes)} bytes")
    
    # Save a copy for debugging
    debug_filename = f"direct_pdf_{token[:8]}.pdf"
    with open(f"/tmp/{debug_filename}", "wb") as f:
        f.write(pdf_bytes)
    
    # Return as direct Response without streaming
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=cv_{token[:8]}.pdf",
            "Content-Type": "application/pdf",
            "Content-Length": str(len(pdf_bytes))
        }
    )

@router.post("/api/download-cv-pdf/")
async def download_cv_pdf_direct_route(cv_text_input: CVTextInput) -> StreamingResponse:
    """
    Direct download endpoint for CV PDF.
    Accepts the CV text input directly and returns the PDF.
    """
    logging.info(f"ENTRY: download_cv_pdf_direct_route called with text length: {len(cv_text_input.cv_text) if cv_text_input.cv_text else 'None'}")
    
    try:
        user_text = cv_text_input.cv_text
        if not user_text:
            logging.error("download_cv_pdf_direct_route received empty cv_text")
            raise HTTPException(status_code=400, detail="CV text cannot be empty")
        
        # Generate token for this download
        token = str(uuid.uuid4())
        logging.info(f"Generated token for direct download: {token[:8]}...")
        
        # Store in temporary_download_urls with 24 hour expiry
        expiry_timestamp = time.time() + 86400  # 24 hours
        temporary_download_urls[token] = {
            "user_text": user_text,
            "expiry_timestamp": expiry_timestamp
        }
        
        logging.info(f"Before generate_cv_content_gemini call")
        ai_cv_content = generate_cv_content_gemini(user_text)
        logging.info(f"After generate_cv_content_gemini: content length = {len(ai_cv_content) if ai_cv_content else 'None'}")
        
        logging.info(f"Before generate_cv_html call")
        html_content = generate_cv_html(ai_cv_content)
        logging.info(f"After generate_cv_html: HTML content length = {len(html_content) if html_content else 'None'}")
        
        logging.info(f"Before convert_html_to_pdf call")
        pdf_bytes = convert_html_to_pdf(html_content)
        if pdf_bytes is None:
            logging.error(f"convert_html_to_pdf returned None!")
        else:
            logging.info(f"After convert_html_to_pdf: PDF size = {len(pdf_bytes)} bytes")
        
        if pdf_bytes:
            logging.info(f"Before creating StreamingResponse: PDF size = {len(pdf_bytes)} bytes")
            
            # --- TEMPORARY SAVE PDF TO DISK for debugging ---
            try:
                filepath = f"/tmp/cv_direct_{token[:8]}.pdf"
                with open(filepath, 'wb') as f:
                    f.write(pdf_bytes)
                logging.info(f"Saved direct PDF to disk for debugging: {filepath}")
            except Exception as e:
                logging.error(f"Error saving direct PDF to disk: {e}")
            # --- END TEMPORARY SAVE ---
            
            return StreamingResponse(
                io.BytesIO(pdf_bytes),
                media_type="application/pdf",
                headers={"Content-Disposition": f"attachment;filename=cv_{token[:8]}.pdf"}
            )
        else:
            logging.error(f"PDF generation failed - pdf_bytes is None!")
            raise HTTPException(status_code=500, detail="PDF generation failed")
    except Exception as e:
        logging.exception(f"Error in direct PDF download: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating PDF: {str(e)}")

# Add a new route that matches the frontend redirect URL structure
@router.get("/download/{token}")
async def download_cv_frontend_route(token: str, request: Request):
    """
    Frontend-friendly download route that matches the URL structure used in the Paymob callback.
    This route simply forwards the request to the main download_cv_pdf_route.
    """
    logging.info(f"Frontend download route hit with token: {token[:8]}...")
    return await download_cv_pdf_route(token, request)
