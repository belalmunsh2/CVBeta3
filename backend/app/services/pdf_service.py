import weasyprint
import logging
import tempfile
import os

logger = logging.getLogger(__name__)

def generate_cv_html(cv_text: str) -> str:
    """
    Generates HTML content for the CV.
    Uses a very basic HTML structure for robust PDF conversion.
    """
    logger.info("generate_cv_html called with text length: %d", len(cv_text) if cv_text else 0)
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Generated CV</title>
        <style>
            body {{ font-family: Arial, sans-serif; }} /* Minimal CSS */
        </style>
    </head>
    <body>
        <h1>CV Title Placeholder</h1>
        <p>{cv_text}</p>
    </body>
    </html>
    """
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