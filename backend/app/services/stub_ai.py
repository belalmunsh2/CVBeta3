from .ai_prompts import CV_SYSTEM_PROMPT

def generate_cv_content_stub(user_text: str) -> str:
    """
    Stub AI function to generate CV content.
    For now, it returns the system prompt itself as a placeholder.
    """
    # In the future, this function will call the actual AI model
    # and use the user_text and system_prompt to generate CV content.
    return CV_SYSTEM_PROMPT # Return the system prompt as stubbed output