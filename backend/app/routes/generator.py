from fastapi import APIRouter, Response
from fastapi.responses import PlainTextResponse, StreamingResponse
from io import BytesIO
from app.models.schemas import CVTextInput
from ..services.gemini_ai_service import generate_cv_content_gemini
from ..services.pdf_service import generate_cv_html, convert_html_to_pdf
import logging

logging.basicConfig(level=logging.INFO)  # Configure basic logging to console
logger = logging.getLogger(__name__)  # Get a logger instance for this module

router = APIRouter()

def parse_cv_content(content: str) -> dict:
    """
    Parse the CV content from markdown-style text into structured sections
    """
    sections = {}
    current_section = None
    current_items = []
    
    for line in content.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        # Check if this is a section header (surrounded by **)
        if line.startswith('**') and line.endswith('**'):
            # If we were building a previous section, save it
            if current_section:
                sections[current_section] = current_items
            
            # Start new section
            current_section = line.strip('*').strip()
            current_items = []
        # Check if this is a bullet point
        elif line.startswith('*'):
            current_items.append(line[1:].strip())
        # Otherwise it's regular text
        else:
            current_items.append(line)
    
    # Don't forget to save the last section
    if current_section:
        sections[current_section] = current_items
        
    return sections

def generate_html_from_ai_content(sections: dict) -> str:
    """Generates HTML string from parsed CV sections."""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simplified CV Test</title>
    </head>
    <body>
        <div class="cv-container">
            <div class="section summary">
                <h2>Summary</h2>
                <p>This is a test summary.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

@router.get("/health")
async def health_check():
    return {"status": "OK"}

@router.post("/generate-cv/")
async def generate_cv(cv_text_input: CVTextInput) -> PlainTextResponse:
    """
    Generates CV content in plain text (temporarily for debugging - NO WEASYPRINT).
    """
    user_text = cv_text_input.user_text
    ai_cv_content = generate_cv_content_gemini(user_text)
    print("Backend: /generate-cv/ - AI generated content (plain text, no PDF):")
    print(ai_cv_content)
    return PlainTextResponse(content=ai_cv_content)

@router.post("/download-cv-pdf/")
async def download_cv_pdf(cv_text_input: CVTextInput):
    """
    Generates CV content using Gemini AI and returns it as a downloadable PDF file.
    """
    user_text = cv_text_input.user_text
    ai_cv_content = generate_cv_content_gemini(user_text)
    html_content = generate_cv_html(ai_cv_content)
    pdf_bytes = convert_html_to_pdf(html_content)

    def iter_pdf_content():
        yield pdf_bytes

    headers = {
        'Content-Disposition': 'attachment; filename="cv.pdf"',
        'Content-Type': 'application/pdf'
    }
    return StreamingResponse(iter_pdf_content(), media_type="application/pdf", headers=headers)

@router.post("/create-payment-session")
async def create_payment_session(cv_text_input: CVTextInput):
    paytabs_api_endpoint_url = "https://secure-egypt.paytabs.com/payment/request"  # Replace with actual PayTabs TEST API endpoint
    headers = {
        "Authorization": "Bearer SDJ9R6HRD2-JK9ZMBJRZH-W9JDNGB66K",  # Replace with your actual Test API Key
        "Content-Type": "application/json"
    }
    request_body_data = {
        "profile_id": "144516",  # Replace with your actual Profile ID
        "tran_type": "sale",
        "tran_class": "ecom",
        "cart_id": "CV-PDF-ORDER-123",  # Placeholder - will be made dynamic later
        "cart_description": "CV PDF Download",
        "cart_currency": "USD",
        "cart_amount": "1.00",
        "callback_url": "http://localhost:5173/payment-success",  # Replace with your actual frontend payment success route URL
        "return_url": "http://localhost:5173/payment-cancel"  # Replace with your actual frontend payment cancel route URL
    }

    try:
        logger.info("Initiating PayTabs API request:")
        logger.info(f"  Endpoint URL: {paytabs_api_endpoint_url}")
        logger.info(f"  Headers: {headers}")
        logger.info(f"  Request Body: {request_body_data}")
        import requests
        response = requests.post(paytabs_api_endpoint_url, headers=headers, json=request_body_data)

        if response:  # Check if response is not None (to avoid errors if request failed completely)
            logger.info(f"PayTabs API Response Status Code: {response.status_code}")
            logger.debug(f"PayTabs API Response Text: {response.text}")  # Use debug for full text
        else:
            logger.error("PayTabs API Response is None (Network Error)")

        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        response_json = response.json()
        payment_url = response_json.get("redirect_url")

        if payment_url:
            return {"payment_url": payment_url}
        else:
            logger.warning("Payment URL not found in PayTabs response")
            return {"error": "Failed to retrieve payment URL from PayTabs"}

    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during PayTabs API call: {e}")  # Log the exception e
        return {"error": "Failed to connect to PayTabs"}
    except Exception as e:
        logger.error(f"Error creating payment session with PayTabs: {e}")  # Log the exception e
        return {"error": "Failed to create payment session with PayTabs"}
