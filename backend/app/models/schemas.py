from pydantic import BaseModel

class CVTextInput(BaseModel):
    user_text: str