from fastapi import APIRouter, Response, HTTPException
from fastapi.responses import PlainTextResponse, StreamingResponse
from pydantic import BaseModel
from typing import Optional
import logging
import requests
import os
from app import config

# Configure logging
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
    
    # Verify Secret key is available
    if not os.environ.get("PAYMOB_SECRET_KEY"):
        logger.error("PAYMOB_SECRET_KEY environment variable not set")
        raise HTTPException(status_code=500, detail="Payment service configuration error")
    
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

def create_paymob_order(amount, currency):
    paymob_api_endpoint_url = "https://accept.paymob.com/v1/intention/"  # Reverted to potentially stable version

    # Get Secret key from environment
    secret_key = os.environ.get("PAYMOB_SECRET_KEY")
    if not secret_key:
        logger.error("PAYMOB_SECRET_KEY environment variable not set")
        return {"error": "Payment service configuration error"}

    headers = {
        "Authorization": f"Token {secret_key}",
        "Content-Type": "application/json"
    }

    request_body_data = {
        "amount": amount,  # Amount in smallest currency unit (piasters for EGP)
        "currency": currency,
        "items": [
            {
                "name": "Test Item",
                "amount": amount,
                "description": "Test item description"
            }
        ]
    }

    try:
        logger.info("Initiating Paymob API request:")
        logger.info(f"  Endpoint URL: {paymob_api_endpoint_url}")
        logger.info(f"  Request Body: {request_body_data}")  # Don't log headers as they contain sensitive info

        response = requests.post(paymob_api_endpoint_url, headers=headers, json=request_body_data)
        response.raise_for_status()
        response_json = response.json()

        logger.info(f"Paymob API Response Status Code: {response.status_code}")
        logger.debug(f"Paymob API Response JSON: {response_json}")

        return response_json

    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during Paymob API call: {e}")
        return {"error": "Failed to connect to Paymob"}
    except Exception as e:
        logger.error(f"Error creating Paymob order: {e}")
        return {"error": "Failed to create Paymob order"}

def generate_payment_key(amount, currency, order_id):
    paymob_api_endpoint_url = "https://accept.paymob.com/v1/intention/"  # Reverted to potentially stable version

    # Get Secret key from environment
    secret_key = os.environ.get("PAYMOB_SECRET_KEY")
    if not secret_key:
        logger.error("PAYMOB_SECRET_KEY environment variable not set")
        return {"error": "Payment service configuration error"}

    headers = {
        "Authorization": f"Token {secret_key}",
        "Content-Type": "application/json"
    }

    request_body_data = {
        "amount": amount,
        "currency": currency,
        "order_id": order_id,
        "integration_id": config.PAYMOB_INTEGRATION_ID,
        "billing_data": {
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "phone_number": "+201234567890"
        }
    }

    try:
        logger.info("Generating payment key:")
        logger.info(f"  Endpoint URL: {paymob_api_endpoint_url}")
        logger.info(f"  Request Body: {request_body_data}")  # Don't log headers as they contain sensitive info

        response = requests.post(paymob_api_endpoint_url, headers=headers, json=request_body_data)
        response.raise_for_status()
        response_json = response.json()

        logger.info(f"Paymob API Response Status Code: {response.status_code}")
        logger.debug(f"Paymob API Response JSON: {response_json}")

        return response_json

    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during Paymob API call: {e}")
        return {"error": "Failed to connect to Paymob"}
    except Exception as e:
        logger.error(f"Error generating payment key: {e}")
        return {"error": "Failed to generate payment key"}
