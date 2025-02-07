import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file - MUST BE FIRST

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set!")