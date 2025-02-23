import logging
import os
import requests
from app import config

logger = logging.getLogger(__name__)

# Payment service functions will be defined here

def create_paymob_order(amount, currency):
    paymob_api_endpoint_url = "https://accept.paymob.com/v1/intention/"

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
        "delivery_needed": False,  # Digital service, no delivery needed
        "items": [
            {
                "name": "Test Item",
                "amount": amount,
                "description": "Test item description"
            }
        ],
        "billing_data": {
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "phone_number": "+201234567890",
            "country": "EGY"  # Egypt country code
        }
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
        
        logger.info(f"Paymob API Response Status Code: {response.status_code}")
        response_json = response.json()
        logger.debug(f"Paymob API Response JSON: {response_json}")

        return response_json

    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during Paymob API call: {e}")
        return {"error": "Failed to connect to Paymob"}
    except Exception as e:
        logger.error(f"Error creating Paymob order: {e}")
        return {"error": "Failed to create Paymob order"}

def generate_payment_key(amount, currency, order_id):
    paymob_api_endpoint_url = "https://accept.paymob.com/api/acceptance/payment_keys"  

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
        logger.info("Initiating Paymob API request:")
        logger.info(f"  Endpoint URL: {paymob_api_endpoint_url}")
        logger.debug(f"  Request Headers (Authorization Token will be logged): {headers}")  # Log headers for auth debugging
        logger.debug(f"  Request Body: {request_body_data}")  # Log request body for data verification

        response = requests.post(paymob_api_endpoint_url, headers=headers, json=request_body_data)
        
        logger.debug("Checking response status for errors...")  # Log before raise_for_status
        logger.debug(f"Paymob API Response Text (before JSON parsing): {response.text}")  # Log raw response text
        response.raise_for_status()
        
        logger.info(f"Paymob API Response Status Code: {response.status_code}")
        response_json = response.json()
        logger.debug(f"Paymob API Response JSON: {response_json}")

        return response_json

    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during Paymob API call: {e}")
        return {"error": "Failed to connect to Paymob"}
    except Exception as e:
        logger.error(f"Error generating payment key: {e}")
        return {"error": "Failed to generate payment key"}
