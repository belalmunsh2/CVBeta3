import weasyprint
import logging
import tempfile
import os
import json

logger = logging.getLogger(__name__)

def generate_cv_html(cv_json: str) -> str:
    """
    Generates HTML content for the CV based on the structured JSON input.
    """
    try:
        cv_data = json.loads(cv_json)
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse CV JSON: {str(e)}")
        return "<html><body><h1>Error: Invalid CV data</h1></body></html>"

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Generated CV</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #2c3e50; }
            h2 { color: #34495e; }
            h3 { color: #7f8c8d; }
            ul { list-style-type: disc; margin-left: 20px; }
            .section { margin-bottom: 20px; }
        </style>
    </head>
    <body>
    """

    # Personal Information
    personal_info = cv_data.get("personal_information", {})
    html_content += f"<h1>{personal_info.get('full_name', 'CV Title Placeholder')}</h1>"
    html_content += "<div class='section'>"
    html_content += "<h2>Personal Information</h2>"
    html_content += f"<p><strong>Email:</strong> {personal_info.get('email', '')}</p>"
    html_content += f"<p><strong>Phone:</strong> {personal_info.get('phone_number', '')}</p>"
    html_content += f"<p><strong>Location:</strong> {personal_info.get('location', '')}</p>"
    html_content += "</div>"

    # Work Experience
    work_experience = cv_data.get("work_experience", [])
    if work_experience:
        html_content += "<div class='section'>"
        html_content += "<h2>Work Experience</h2>"
        for job in work_experience:
            html_content += f"<h3>{job.get('job_title', '')} at {job.get('company_name', '')}</h3>"
            html_content += f"<p><strong>{job.get('start_date', '')} - {job.get('end_date', '')}</strong></p>"
            html_content += "<ul>"
            for resp in job.get("responsibilities", []):
                html_content += f"<li>{resp}</li>"
            html_content += "</ul>"
        html_content += "</div>"

    # Education
    education = cv_data.get("education", [])
    if education:
        html_content += "<div class='section'>"
        html_content += "<h2>Education</h2>"
        for edu in education:
            html_content += f"<h3>{edu.get('degree', '')}</h3>"
            html_content += f"<p>{edu.get('institution', '')}, {edu.get('graduation_date', '')}</p>"
        html_content += "</div>"

    # Skills & Summary
    skills_summary = cv_data.get("skills_summary", {})
    if skills_summary:
        html_content += "<div class='section'>"
        html_content += "<h2>Skills & Summary</h2>"
        html_content += "<ul>"
        for skill in skills_summary.get("skills", []):
            html_content += f"<li>{skill}</li>"
        html_content += "</ul>"
        html_content += f"<p><strong>Summary:</strong> {skills_summary.get('summary', '')}</p>"
        html_content += "</div>"

    # Certifications
    certifications = cv_data.get("certifications", [])
    if certifications:
        html_content += "<div class='section'>"
        html_content += "<h2>Certifications</h2>"
        html_content += "<ul>"
        for cert in certifications:
            html_content += f"<li>{cert}</li>"
        html_content += "</ul>"
        html_content += "</div>"

    # Projects
    projects = cv_data.get("projects", [])
    if projects:
        html_content += "<div class='section'>"
        html_content += "<h2>Projects</h2>"
        for project in projects:
            html_content += f"<h3>{project.get('title', '')}</h3>"
            html_content += f"<p>{project.get('description', '')}</p>"
        html_content += "</div>"

    # Social/Professional Links
    social_links = cv_data.get("social_links", {})
    if social_links:
        html_content += "<div class='section'>"
        html_content += "<h2>Social/Professional Links</h2>"
        for key, value in social_links.items():
            html_content += f"<p><strong>{key.capitalize()}:</strong> <a href='{value}'>{value}</a></p>"
        html_content += "</div>"

    html_content += "</body></html>"
    logger.info("HTML generation complete, length: %d", len(html_content))
    return html_content

def convert_html_to_pdf(html_string: str) -> bytes:
    """
    Converts an HTML string to a PDF file in bytes format using WeasyPrint.
    Simplified WeasyPrint call for potential fix.

    Args:
        html_string: A string containing the HTML content to convert.

    Returns:
        bytes: The PDF file content as bytes.
    """
    if not html_string:
        logger.error("convert_html_to_pdf received empty HTML string")
        return None
        
    logger.info("Starting PDF conversion with WeasyPrint, HTML length: %d", len(html_string))
    
    try:
        # First, save HTML to a temporary file for debugging
        with tempfile.NamedTemporaryFile(delete=False, suffix='.html', mode='w+', encoding='utf-8') as f:
            f.write(html_string)
            html_path = f.name
        
        logger.info("Saved HTML to temporary file: %s", html_path)
        
        # Try with string method
        logger.info("Attempting PDF conversion using HTML(string=html_string)")
        pdf_bytes = weasyprint.HTML(string=html_string).write_pdf()
        
        # Log the size of the resulting PDF
        logger.info("PDF conversion complete, size: %d bytes", len(pdf_bytes) if pdf_bytes else 0)
        
        if pdf_bytes and len(pdf_bytes) < 100:
            logger.error(f"Generated PDF is suspiciously small: {len(pdf_bytes)} bytes")
            
            # If first method produced a small PDF, try with the file method as fallback
            logger.info("Attempting PDF conversion using HTML(filename=html_path)")
            pdf_bytes = weasyprint.HTML(filename=html_path).write_pdf()
            logger.info("File-based PDF conversion complete, size: %d bytes", len(pdf_bytes) if pdf_bytes else 0)
            
            if pdf_bytes and len(pdf_bytes) < 100:
                logger.error(f"File-based PDF is also suspiciously small: {len(pdf_bytes)} bytes")
                return None
        
        # Also save the PDF to a temporary file for inspection
        if pdf_bytes:
            pdf_path = html_path.replace('.html', '.pdf')
            with open(pdf_path, 'wb') as f:
                f.write(pdf_bytes)
            logger.info("Saved PDF to temporary file: %s", pdf_path)
        
        return pdf_bytes
    except Exception as e:
        logger.exception(f"Error in PDF conversion: {str(e)}")
        return None