from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional, Any
import logging
import os
import requests
import uuid
import time
from app import config
from ..services.payment_service import create_paymob_order
from ..routes.pdf_routes import temporary_download_urls

logger = logging.getLogger(__name__)
router = APIRouter()

class BillingData(BaseModel):
    email: str
    first_name: str
    last_name: str
    phone_number: str
    country: str

class Item(BaseModel):
    name: str
    amount: int
    description: str
    quantity: int = 1

class PaymentSessionRequest(BaseModel):
    amount: int
    currency: str = "EGP"
    billing_data: Optional[BillingData] = None
    items: Optional[List[Item]] = None
    user_text: Optional[str] = None

@router.post("/create-payment-session")
async def create_payment_session(payload: PaymentSessionRequest):
    """
    Creates a payment session with Paymob using the provided amount.
    Amount should be in smallest currency unit (e.g., cents for USD, piasters for EGP)
    """
    logger = logging.getLogger(__name__)
    
    # Generate download_token BEFORE payment session
    download_token = str(uuid.uuid4())
    
    # Store user_text in temporary_download_urls if provided
    if payload.user_text:
        temporary_download_urls[download_token] = {
            "user_text": payload.user_text,
            "expiry_timestamp": time.time() + 1800  # 30 minutes expiry
        }
        logger.info(f"Stored user_text with download_token: {download_token}")
    
    # Extract billing_data and items if provided
    billing_data = payload.billing_data.dict() if payload.billing_data else None
    items = [item.dict() for item in payload.items] if payload.items else None
    
    # Step 1: Create Order with Intention API
    order_response = create_paymob_order(
        payload.amount, 
        payload.currency,
        billing_data=billing_data,
        items=items
    )
    
    if "error" in order_response:
        logger.error(f"Failed to create Paymob order: {order_response['error']}")
        raise HTTPException(status_code=400, detail=order_response["error"])
    
    # Return client_secret directly from the Intention API response
    if "client_secret" in order_response:
        logger.info(f"Successfully created payment intention with client_secret")
        # Add public_key and payment_url to the response
        return {
            "client_secret": order_response["client_secret"],
            "public_key": config.PAYMOB_PUBLIC_KEY,
            "payment_url": "https://accept.paymob.com/unifiedcheckout/",
            "download_token": download_token
        }
    else:
        logger.error("Client secret not found in Paymob response")
        raise HTTPException(status_code=400, detail="Invalid response from payment provider")
