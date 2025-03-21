import logging
import os
import requests
from app import config
import uuid
import time

logger = logging.getLogger(__name__)

# Payment service functions will be defined here

def create_paymob_order(amount, currency, billing_data=None, items=None):
    paymob_api_endpoint_url = "https://accept.paymob.com/v1/intention/"

    # Get Secret key from config
    secret_key = config.PAYMOB_SECRET_KEY

    headers = {
        "Authorization": f"Token {secret_key}",
        "Content-Type": "application/json"
    }

    # Use provided billing_data or default
    if not billing_data:
        billing_data = {
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "phone_number": "+201234567890"
        }

    # Use provided items or default
    if not items:
        items = [
            {
                "name": "CV Generation Service",
                "amount": amount,
                "description": "AI-Powered CV Generation",
                "quantity": 1
            }
        ]

    # Complete the billing data with required fields
    complete_billing_data = {
        "apartment": "sympl",
        "street": "dumy",
        "building": "dumy",
        "city": "dumy",
        "country": "EG",
        "floor": "dumy",
        "state": "dumy",
        # Override with provided billing data
        "email": billing_data.get("email", "test@example.com"),
        "first_name": billing_data.get("first_name", "Test"),
        "last_name": billing_data.get("last_name", "User"),
        "phone_number": billing_data.get("phone_number", "+201234567890")
    }

    # Create customer data from billing data
    customer = {
        "first_name": billing_data.get("first_name", "Test"),
        "last_name": billing_data.get("last_name", "User"),
        "email": billing_data.get("email", "test@example.com"),
        "extras": {}
    }

    request_body_data = {
        "amount": amount,
        "currency": currency,
        "payment_methods": [4926084, 4912622],  # Card and ValU payment methods
        "items": items,
        "billing_data": complete_billing_data,
        "customer": customer,
        "extras": {}
    }

    try:
        logger.info("Initiating Paymob API request:")
        logger.info(f"  Endpoint URL: {paymob_api_endpoint_url}")
        logger.debug(f"  Request Headers (Authorization Token will be logged): {headers}")  # Log headers for auth debugging
        logger.debug(f"  Request Body: {request_body_data}")  # Log request body for data verification

        response = requests.post(paymob_api_endpoint_url, headers=headers, json=request_body_data)
        
        logger.debug("Checking response status for errors...")  # Log before raise_for_status
        logger.debug(f"Paymob API Response Text (before JSON parsing): {response.text}")  # Log raw response text
        response.raise_for_status()
        
        response_json = response.json()
        logger.info(f"Paymob Intention API Full Response JSON: {response_json}")  
        logger.info(f"Paymob API Response Status Code: {response.status_code}")
        logger.debug(f"Paymob API Response JSON: {response_json}")

        # Check if client_secret exists for logging purposes
        client_secret = response_json.get('client_secret')
        if not client_secret:
            logger.error(f"Paymob API responded successfully, but 'client_secret' not found in response JSON. Response JSON: {response_json}")
        
        # Return the full response_json instead of just the client_secret
        return response_json

    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during Paymob API call: {e}")
        return {"error": "Failed to connect to Paymob"}
    except Exception as e:
        logger.error(f"Error creating Paymob order: {e}")
        return {"error": "Failed to create Paymob order"}