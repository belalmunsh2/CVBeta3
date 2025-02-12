from fastapi import APIRouter, Response
from fastapi.responses import PlainTextResponse, StreamingResponse
from io import BytesIO
from app.models.schemas import CVTextInput
from ..services.gemini_ai_service import generate_cv_content_gemini
from ..services.pdf_service import generate_cv_html, convert_html_to_pdf

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
