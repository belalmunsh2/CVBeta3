import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file - MUST BE FIRST

# Load Gemini API Key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set!")

# Load Paymob API Keys and Integration ID
PAYMOB_PUBLIC_KEY = os.environ.get("PAYMOB_PUBLIC_KEY")
if not PAYMOB_PUBLIC_KEY:
    raise ValueError("PAYMOB_PUBLIC_KEY environment variable not set!")

PAYMOB_INTEGRATION_ID = os.environ.get("PAYMOB_INTEGRATION_ID")
if not PAYMOB_INTEGRATION_ID:
    raise ValueError("PAYMOB_INTEGRATION_ID environment variable not set!")