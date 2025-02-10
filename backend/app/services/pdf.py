import weasyprint

def generate_pdf_from_html(html_content: str) -> bytes:
    """
    Generates a PDF from HTML content using WeasyPrint.

    Args:
        html_content: A string containing HTML content.

    Returns:
        bytes: The PDF content as bytes.
    """
    pdf_file = weasyprint.HTML(string=html_content).write_pdf()
    return pdf_file