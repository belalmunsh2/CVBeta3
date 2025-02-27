import google.generativeai as genai
from app import config
from .ai_prompts import CV_SYSTEM_PROMPT

# Configure the Gemini API key
genai.configure(api_key=config.GEMINI_API_KEY)

# Load the Gemini Pro model with explicit API version
model = genai.GenerativeModel('models/gemini-pro-v1beta', api_version='v1beta')

def generate_cv_content_gemini(user_text: str) -> str:
    """
    Generates CV content using the Google Gemini AI API.
    """
    try:
        full_prompt = CV_SYSTEM_PROMPT + "\n\nUser CV Text:\n" + user_text
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        print(f"Error during Gemini API call: {e}") # Log the error for debugging
        return "Error generating CV content with Gemini API. Please try again later."
