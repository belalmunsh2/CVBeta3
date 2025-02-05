# Core service combining AI and PDF logic
from tenacity import retry
import google.generativeai as genai

class CVGenerator:
    @retry
    def generate_ats_content(self, user_input: str) -> str:
        """Process user input with Gemini API"""
        # Implementation will follow
        pass
