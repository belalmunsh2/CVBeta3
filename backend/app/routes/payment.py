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
    Creates a payment session with Paymob and associates download token with order_id.
    """
    logger = logging.getLogger(__name__)
    
    # Generate download_token BEFORE payment session
    download_token = str(uuid.uuid4())
    
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
    
    # *** ENHANCED ERROR HANDLING START ***
    logger.info(f"Paymob order_response just before order_id extraction: {order_response}")  # Log full response
    
    order_id = order_response.get('intention_order_id')  # Get intention_order_id
    
    if not order_id:
        logger.error("Order ID not found in Paymob Intention API response.")
        # *** ENHANCED ERROR MESSAGE - INCLUDE order_response in detail ***
        raise HTTPException(status_code=500, detail=f"Could not retrieve order ID from payment provider. Paymob Response: {order_response}")
    # *** ENHANCED ERROR HANDLING END ***
    
    # Store download_token in temporary_download_urls using order_id as key
    if payload.user_text:
        temporary_download_urls[str(order_id)] = {  # Use order_id as key (convert to string)
            "user_text": payload.user_text,
            "download_token": download_token,  # Store download_token in the data
            "expiry_timestamp": time.time() + 1800  # 30 minutes expiry
        }
        logger.info(f"Stored user_text with download_token: {download_token} for order_id: {order_id}")
    
    # Return client_secret directly from the Intention API response
    if "client_secret" in order_response:
        logger.info(f"Successfully created payment intention with client_secret for order_id: {order_id}")
        # Add public_key and payment_url to the response
        return {
            "client_secret": order_response["client_secret"],
            "public_key": config.PAYMOB_PUBLIC_KEY,
            "payment_url": "https://accept.paymob.com/unifiedcheckout/",
            "download_token": download_token,
            "order_id": order_id  # Return order_id in response (might be useful for frontend debugging later)
        }
    else:
        logger.error("Client secret not found in Paymob response")
        raise HTTPException(status_code=400, detail="Invalid response from payment provider")
