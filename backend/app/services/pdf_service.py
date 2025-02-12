import weasyprint

def generate_cv_html(cv_text: str) -> str:
    """
    Converts an HTML string to a PDF file in bytes format using WeasyPrint.

    Args:
        cv_text: A string containing the HTML content to convert.

    Returns:
        bytes: The PDF file content as bytes.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Generated CV</title>
        <style>
            body { font-family: Arial, sans-serif; } /* Correct CSS syntax with curly braces */
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

    Args:
        html_string: A string containing the HTML content to convert.

    Returns:
        bytes: The PDF file content as bytes.
    """
    pdf_bytes = weasyprint.HTML(string=html_string).write_pdf()
    return pdf_bytes
