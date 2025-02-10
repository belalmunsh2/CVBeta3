from fastapi import APIRouter, Response
from app.models.schemas import CVTextInput
from ..services.gemini_ai_service import generate_cv_content_gemini
from ..services.pdf import generate_pdf_from_html

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
    print("Backend: /generate-cv/ - AI generated content:")
    print(ai_cv_content)

    # Parse the CV content into sections
    sections = parse_cv_content(ai_cv_content)
    
    # Generate structured HTML
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Generated CV</title>
    </head>
    <body>
        <div class="cv-container">
            <div class="header">
                <h1>{sections.get('Personal Information', [''])[0]}</h1>
                <p>{sections.get('Contact', [''])[0]}</p>
            </div>

            <div class="section summary">
                <h2>Summary</h2>
                <p>{''.join(sections.get('Summary', []))}</p>
            </div>

            <div class="section experience">
                <h2>Experience</h2>
                {''.join(f"<div class='experience-item'><p>{item}</p></div>" 
                        for item in sections.get('Experience', []))}
            </div>

            <div class="section education">
                <h2>Education</h2>
                {''.join(f"<div class='education-item'><p>{item}</p></div>" 
                        for item in sections.get('Education', []))}
            </div>

            <div class="section skills">
                <h2>Skills</h2>
                <ul>
                    {''.join(f"<li>{item}</li>" for item in sections.get('Skills', []))}
                </ul>
            </div>

            <div class="section projects">
                <h2>Projects</h2>
                {''.join(f"<div class='project-item'><p>{item}</p></div>" 
                        for item in sections.get('Projects', []))}
            </div>
        </div>
    </body>
    </html>
    """

    print(f"Backend: /generate-cv/ - HTML Content for PDF Generation:\n{html_content}")

    print("Backend: /generate-cv/ - Starting PDF generation process...")

    try:
        # Generate PDF from HTML
        pdf_bytes = generate_pdf_from_html(html_content)
        print("Backend: /generate-cv/ - PDF generation successful.")

        # Return PDF file as a response
        return Response(content=pdf_bytes, media_type="application/pdf", 
                      headers={"Content-Disposition": "attachment; filename=generated_cv.pdf"})

    except Exception as e:
        print(f"Backend: /generate-cv/ - ERROR during PDF generation: {e}")
        return Response(content="Error generating PDF", status_code=500, media_type="text/plain")


@router.get("/generate_test_pdf")
async def generate_test_pdf() -> Response:
    """
    Generates a simple test PDF using WeasyPrint and returns it as a downloadable file.
    """
    html_content = "<h1>Hello from WeasyPrint!</h1><p>This is a test PDF.</p>"
    print("Backend: /generate_test_pdf - Starting test PDF generation...")
    pdf_bytes = generate_pdf_from_html(html_content)
    print("Backend: /generate_test_pdf - Test PDF generation successful.")
    return Response(content=pdf_bytes, media_type="application/pdf", 
                   headers={"Content-Disposition": "attachment; filename=test_pdf.pdf"})