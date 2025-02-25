import os
from dotenv import load_dotenv
import logging

load_dotenv()  # Load environment variables from .env file - MUST BE FIRST

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load Gemini API Key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set!")
logger.info(f"Config Value - GEMINI_API_KEY: {GEMINI_API_KEY}")

# Load Paymob API Keys and Integration ID
logger.info("--- Config Values at Startup ---")
PAYMOB_PUBLIC_KEY = os.environ.get("PAYMOB_PUBLIC_KEY")
if not PAYMOB_PUBLIC_KEY:
    raise ValueError("PAYMOB_PUBLIC_KEY environment variable not set!")
logger.info(f"Config Value - PAYMOB_PUBLIC_KEY: {PAYMOB_PUBLIC_KEY}")

PAYMOB_SECRET_KEY = os.environ.get("PAYMOB_SECRET_KEY")
if not PAYMOB_SECRET_KEY:
    raise ValueError("PAYMOB_SECRET_KEY environment variable not set!")
logger.info(f"Config Value - PAYMOB_SECRET_KEY: {PAYMOB_SECRET_KEY}")

PAYMOB_INTEGRATION_ID = os.environ.get("PAYMOB_INTEGRATION_ID")
if not PAYMOB_INTEGRATION_ID:
    raise ValueError("PAYMOB_INTEGRATION_ID environment variable not set!")
logger.info(f"Config Value - PAYMOB_INTEGRATION_ID: {PAYMOB_INTEGRATION_ID}")