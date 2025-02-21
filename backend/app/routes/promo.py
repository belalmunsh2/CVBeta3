from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import logging
from ..services.promo_service import validate_promo_code

# Configure logging
logger = logging.getLogger(__name__)

# Create router instance
router = APIRouter()

class PromoCodeRequest(BaseModel):
    """Request model for promo code validation"""
    promo_code: str
    amount: int  # Amount in cents

class PromoCodeResponse(BaseModel):
    """Response model for promo code validation"""
    discounted_amount: int | None = None
    discount_percentage: float | None = None
    original_amount: int | None = None
    error: str | None = None

@router.post("/apply-coupon", response_model=PromoCodeResponse)
async def apply_coupon(request: PromoCodeRequest) -> PromoCodeResponse:
    """
    Apply a promo code to get discounted amount
    
    Args:
        request (PromoCodeRequest): Contains promo_code and amount
        
    Returns:
        PromoCodeResponse: Contains discounted amount and discount percentage or error
    """
    logger.info(f"Received promo code application request: {request}")
    
    try:
        result = validate_promo_code(request.promo_code, request.amount)
        
        if "error" in result:
            logger.warning(f"Promo code validation failed: {result['error']}")
            return PromoCodeResponse(error=result["error"])
            
        logger.info(f"Successfully applied promo code: {request.promo_code}")
        return PromoCodeResponse(
            discounted_amount=result["discounted_amount"],
            discount_percentage=result["discount_percentage"],
            original_amount=result["original_amount"]
        )
        
    except Exception as e:
        logger.error(f"Error processing promo code: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing the promo code"
        )
