from fastapi import APIRouter, Response
from app.models.schemas import CVTextInput
from ..services.gemini_ai_service import generate_cv_content_gemini
from ..services.pdf import generate_pdf_from_html

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "OK"}

@router.post("/generate-cv/")
async def generate_cv(cv_text_input: CVTextInput) -> Response:
    """
    Generates a CV in PDF format based on user input.
    """
    user_text = cv_text_input.user_text
    ai_cv_content = generate_cv_content_gemini(user_text)
    print("Backend: /generate-cv/ - AI generated content:")  # Add this logging line
    print(ai_cv_content) # Log the actual AI content - VERY IMPORTANT

    # Convert CV content to basic HTML (using <pre> for now)
    html_content = f"<pre>{ai_cv_content}</pre>"  # Access data using dictionary key
    print(f"Backend: /generate-cv/ - HTML Content for PDF Generation:\n{html_content}")

    print("Backend: /generate-cv/ - Starting PDF generation process...")  # Log start of PDF generation

    try:
        # Generate PDF from HTML
        pdf_bytes = generate_pdf_from_html(html_content)
        print("Backend: /generate-cv/ - PDF generation successful.") # Log PDF generation success

        # Return PDF file as a response
        return Response(content=pdf_bytes, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=generated_cv.pdf"})

    except Exception as e:
        print(f"Backend: /generate-cv/ - ERROR during PDF generation: {e}") # Log any errors!
        return Response(content="Error generating PDF", status_code=500, media_type="text/plain") # Return error response


@router.get("/generate_test_pdf")
async def generate_test_pdf() -> Response:
    """
    Generates a simple test PDF using WeasyPrint and returns it as a downloadable file.
    """
    html_content = "<h1>Hello from WeasyPrint!</h1><p>This is a test PDF.</p>"
    print("Backend: /generate_test_pdf - Starting test PDF generation...") # Log start of test PDF
    pdf_bytes = generate_pdf_from_html(html_content)
    print("Backend: /generate_test_pdf - Test PDF generation successful.") # Log test PDF success
    return Response(content=pdf_bytes, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=test_pdf.pdf"})