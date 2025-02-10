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

    # Convert CV content to basic HTML (using <pre> for now)
    html_content = f"<pre>{ai_cv_content}</pre>"  # Access data using dictionary key

    # Generate PDF from HTML
    pdf_bytes = generate_pdf_from_html(html_content)

    # Return PDF file as a response
    return Response(content=pdf_bytes, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=generated_cv.pdf"})

@router.get("/generate_test_pdf")
async def generate_test_pdf() -> Response:
    """
    Generates a simple test PDF using WeasyPrint and returns it as a downloadable file.
    """
    html_content = "<h1>Hello from WeasyPrint!</h1><p>This is a test PDF.</p>"
    pdf_bytes = generate_pdf_from_html(html_content)
    return Response(content=pdf_bytes, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=test_pdf.pdf"})