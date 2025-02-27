import google.generativeai as genai
from app import config
from .ai_prompts import CV_SYSTEM_PROMPT
import logging

logger = logging.getLogger(__name__)

def generate_cv_content_gemini(user_text: str) -> str:
    """
    Generates CV content using the Google Gemini AI API.
    """
    try:
        genai.configure(api_key=config.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini/gemini-1.5-pro')
        full_prompt = CV_SYSTEM_PROMPT + "\n\nUser CV Text:\n" + user_text
        response = model.generate_content(full_prompt)
        logger.info("Successfully generated CV content.")
        return response.text
    except Exception as e:
        logger.exception("Error generating CV content with Gemini:")
        return "Error generating CV content with Gemini API. Please try again later."
