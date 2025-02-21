import logging
from typing import Dict, Optional, Union

# Configure logging
logger = logging.getLogger(__name__)

# In-memory storage for coupons (will be replaced with DB later)
COUPONS: Dict[str, Dict] = {
    "WELCOME10": {
        "discount_percentage": 10,
        "active": True
    },
    "BETA20": {
        "discount_percentage": 20,
        "active": True
    }
}

def get_coupon(code: str) -> Optional[Dict]:
    """
    Retrieve a coupon by its code from the in-memory storage
    
    Args:
        code (str): The promo code to look up
        
    Returns:
        Optional[Dict]: Coupon data if found, None otherwise
    """
    logger.info(f"Looking up coupon with code: {code}")
    return COUPONS.get(code.upper())

def validate_promo_code(code: str, amount: int) -> Dict[str, Union[int, float, str]]:
    """
    Validate a promo code and calculate the discounted amount
    
    Args:
        code (str): The promo code to validate
        amount (int): The original amount in cents
        
    Returns:
        Dict with either:
        - discounted_amount and discount_percentage if valid
        - error message if invalid
    """
    logger.info(f"Validating promo code: {code} for amount: {amount}")
    
    if not code or not amount:
        logger.warning("Invalid input: code or amount is empty")
        return {"error": "Invalid input parameters"}
    
    coupon = get_coupon(code)
    
    if not coupon:
        logger.warning(f"Promo code not found: {code}")
        return {"error": "Promo code invalid"}
        
    if not coupon.get("active", False):
        logger.warning(f"Promo code inactive: {code}")
        return {"error": "Promo code inactive"}
    
    discount_percentage = coupon["discount_percentage"]
    discounted_amount = int(amount * (1 - discount_percentage / 100))
    
    logger.info(f"Calculated discount: {discount_percentage}% for amount: {amount}")
    logger.info(f"Discounted amount: {discounted_amount}")
    
    return {
        "discounted_amount": discounted_amount,
        "discount_percentage": discount_percentage,
        "original_amount": amount
    }
