from fastapi import APIRouter, Response
from fastapi.responses import PlainTextResponse, StreamingResponse
from io import BytesIO
from app.models.schemas import CVTextInput
from ..services.gemini_ai_service import generate_cv_content_gemini
from ..services.pdf_service import generate_cv_html, convert_html_to_pdf
import logging
import requests
import os

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
def create_payment_session():
    logger = logging.getLogger(__name__)

    paymob_api_endpoint_url = "https://accept.paymob.com/v1/intention/"  # Correct Paymob API endpoint

    headers = {
        "Authorization": "Token egy_sk_test_9586098f4302f1cbcb991b99ce26b04e8a864faeed484bbc12ae51c3bbadd182",  # Your Secret Key
        "Content-Type": "application/json"
    }

    request_body_data = {
        "amount": 1000,  # Amount in smallest currency unit (piasters for EGP)
        "currency": "EGP",
        "payment_methods": [4912622],  # Your Integration ID
        "billing_data": {
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "phone_number": "+201234567890"
        },
        "callback_url": "https://webhook.site/e9043d7d-5494-4880-8a89-b45e9a74551d"  # Your webhook.site URL
    }

    try:
        logger.info("Initiating Paymob API request:")
        logger.info(f"  Endpoint URL: {paymob_api_endpoint_url}")
        logger.info(f"  Headers: {headers}")
        logger.info(f"  Request Body: {request_body_data}")

        response = requests.post(paymob_api_endpoint_url, headers=headers, json=request_body_data)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        response_json = response.json()

        logger.info(f"Paymob API Response Status Code: {response.status_code}")
        logger.debug(f"Paymob API Response JSON: {response_json}")

        # Get the payment URL from the response
        payment_url = response_json.get("redirection_url")
        if not payment_url:
            logger.error("Redirection URL not found in Paymob response")
            logger.debug(f"Response keys available: {response_json.keys()}")
            return {"error": "Payment URL not found in provider response"}

        # Get the required keys for payment
        client_secret = response_json.get("client_secret")
        if not client_secret:
            logger.error("Client secret not found in Paymob response")
            return {"error": "Client secret not found in provider response"}

        # Return all necessary data for frontend to construct the complete payment URL
        return {
            "payment_url": payment_url,
            "client_secret": client_secret,
            "public_key": os.environ.get("PAYMOB_PUBLIC_KEY")
        }

    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during Paymob API call: {e}")
        return {"error": "Failed to connect to payment provider"}
    except Exception as e:
        logger.error(f"Error creating payment session: {e}")
        return {"error": "Failed to create payment session"}
