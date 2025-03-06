import weasyprint
import logging

def generate_cv_html(cv_text: str) -> str:
    """
    Generates HTML content for the CV.
    Uses proper HTML5 structure with improved styling for better PDF output.
    """
    # Format paragraphs properly by replacing newlines with <br> tags
    formatted_text = cv_text.replace('\n', '<br />')
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional CV</title>
    <style>
        body {{
            font-family: 'Arial', 'Helvetica', sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 20px;
        }}
        h1 {{
            color: #2563eb;
            border-bottom: 1px solid #e5e7eb;
            padding-bottom: 10px;
            margin-top: 0;
        }}
        h2 {{
            color: #1e40af;
            margin-top: 20px;
            margin-bottom: 10px;
        }}
        p {{
            margin-bottom: 10px;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 30px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        .section {{
            margin-bottom: 25px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Professional CV</h1>
        <div class="section">
            {formatted_text}
        </div>
    </div>
</body>
</html>"""
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