import weasyprint

def generate_pdf_from_html(html_content: str) -> bytes:
    """
    Generates a PDF from HTML content using WeasyPrint.
    Returns the PDF as bytes.
    """
    try:
        pdf_bytes = weasyprint.HTML(string=html_content).write_pdf()
        return pdf_bytes
    except Exception as e:
        print(f"ERROR in generate_pdf_from_html: PDF generation failed! Exception Type: {type(e)}, Exception: {e}") # Detailed error logging
        return None # Or return b'' (empty bytes), or raise the exception again