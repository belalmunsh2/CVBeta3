from pydantic import BaseModel
from typing import Optional

class CVTextInput(BaseModel):
    user_text: str

class PromoCodeRequest(BaseModel):
    promo_code: str
    amount: int  # Am ount  in smallest currency unit

class PromoCodeResponse(BaseModel):
    discounted_amount: Optional[int] = None
    discount_percentage: Optional[float] = None
    original_amount: Optional[int] = None
    message: Optional[str] = None  # Optional success/error message
    error: Optional[str] = None  # For error cases