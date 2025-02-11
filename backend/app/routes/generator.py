from fastapi import APIRouter
from app.models.schemas import CVTextInput
from ..services.gemini_ai_service import generate_cv_content_gemini

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "OK"}

@router.post("/generate-cv/")
async def generate_cv(cv_text_input: CVTextInput) -> str:
    """
    Endpoint to generate CV content using Gemini AI API.
    """
    user_text = cv_text_input.user_text
    print(f"Received user_text from frontend: {user_text}") # <-- MAKE SURE THIS LINE IS *NOT* COMMENTED OUT

    # Construct Prompt (show how prompt is constructed or loaded)
    # ... (Add code here to show how you are constructing the prompt string,
    #      especially if it involves the user_text) ...
    # Example (if prompt is a simple string):
    # prompt = f"Generate a CV based on this text: {user_text}"
    # print(f"Prompt sent to Gemini AI: {prompt}") # <-- MAKE SURE THIS LINE (or similar prompt logging) IS *NOT* COMMENTED OUT

    ai_cv_content = generate_cv_content_gemini(user_text) # Pass user_text to AI service
    print(f"AI generated CV content: {ai_cv_content}") # <-- MAKE SURE THIS LINE IS *NOT* COMMENTED OUT

    return ai_cv_content