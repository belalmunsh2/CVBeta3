import weasyprint
import logging

def generate_cv_html(cv_text: str) -> str:
    """
    Generates HTML content for the CV.
    Uses a very basic HTML structure for robust PDF conversion.
    """
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
    return html_content

def convert_html_to_pdf(html_string: str) -> bytes:
    """
    Converts an HTML string to a PDF file in bytes format using WeasyPrint.
    Added error handling and explicit encoding settings.

    Args:
        html_string: A string containing the HTML content to convert.

    Returns:
        bytes: The PDF file content as bytes.
    """
    try:
        # Use explicit encoding and include proper CSS base URL
        html = weasyprint.HTML(string=html_string, encoding='utf-8')
        pdf_bytes = html.write_pdf(optimize_size=('fonts',))
        
        # Verify the PDF is not empty
        if len(pdf_bytes) < 100:  # Very small PDFs are likely corrupted
            logging.error(f"Generated PDF is suspiciously small: {len(pdf_bytes)} bytes")
            return None
            
        return pdf_bytes
    except Exception as e:
        logging.exception(f"Error in PDF conversion: {str(e)}")
        return None