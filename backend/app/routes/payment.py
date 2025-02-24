from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import logging
import os
import requests
from app import config
from ..services.payment_service import create_paymob_order, generate_payment_key

logger = logging.getLogger(__name__)
router = APIRouter()

class PaymentSessionRequest(BaseModel):
    amount: int
    currency: str = "EGP"

@router.post("/create-payment-session")
async def create_payment_session(payload: PaymentSessionRequest):
    """
    Creates a payment session with Paymob using the provided amount.
    Amount should be in smallest currency unit (e.g., cents for USD, piasters for EGP)
    """
    logger = logging.getLogger(__name__)
    
    # Step 1: Create Order
    order_response = create_paymob_order(payload.amount, payload.currency)
    if "error" in order_response:
        logger.error(f"Failed to create Paymob order: {order_response['error']}")
        raise HTTPException(status_code=400, detail=order_response["error"])
    
    order_id = order_response.get("id")
    if not order_id:
        logger.error("Order ID not found in Paymob response")
        raise HTTPException(status_code=400, detail="Invalid response from payment provider")

    # Step 2: Generate Payment Key
    payment_key_response = generate_payment_key(payload.amount, payload.currency, order_id)
    if "error" in payment_key_response:
        logger.error(f"Failed to generate payment key: {payment_key_response['error']}")
        raise HTTPException(status_code=400, detail=payment_key_response["error"])
    
    token = payment_key_response.get("token")
    if not token:
        logger.error("Payment token not found in Paymob response")
        raise HTTPException(status_code=400, detail="Invalid response from payment provider")

    # Step 3: Construct Hosted Payment Page URL
    payment_url = f"https://accept.paymob.com/api/acceptance/iframes/{config.PAYMOB_INTEGRATION_ID}?payment_token={token}"
    
    logger.info(f"Successfully created payment session. URL: {payment_url}")
    return {
        "payment_url": payment_url,
        "public_key": os.environ.get("PAYMOB_PUBLIC_KEY")
    }
