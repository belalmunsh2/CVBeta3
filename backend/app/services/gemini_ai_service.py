import google.generativeai as genai
from app import config
from .ai_prompts import CV_SYSTEM_PROMPT
import logging

logger = logging.getLogger(__name__)


def generate_cv_content_gemini(user_text: str) -> str:
    """
    Generates CV content using the Gemini Pro model.
    Args:
        user_text (str): The user-provided text for generating CV content.
    Returns:
        str: The generated CV content.
    """
    try:
        genai.configure(api_key=config.GEMINI_API_KEY)
        project_id = "gen-lang-client-0902987432"  # Your Google Cloud Project ID
        location = "us-central1"  # Google Cloud location (try us-central1 initially)
        model_name = f"projects/{project_id}/locations/{location}/models/gemini-2.0-flash"
        model = genai.GenerativeModel(model_name)
        full_prompt = CV_SYSTEM_PROMPT + "\n\nUser CV Text:\n" + user_text
        response = model.generate_content(full_prompt)
        logger.info("Successfully generated CV content.")
        return response.text
    except Exception as e:
        logger.exception("Error generating CV content with Gemini:")
        return "Error generating CV content with Gemini API. Please try again later."
