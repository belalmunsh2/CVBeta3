import logging
import os
import requests
from app import config

logger = logging.getLogger(__name__)

# Payment service functions will be defined here

def get_paymob_auth_token():
    auth_url = "https://accept.paymob.com/api/auth/tokens"
    headers = {"Content-Type": "application/json"}  # Headers for auth request
    request_body = {"api_key": config.PAYMOB_SECRET_KEY}  # API Key in request body

    try:
        logger.info("Initiating Paymob Authentication Token Request...")  # Log auth request
        response = requests.post(auth_url, headers=headers, json=request_body)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        auth_response_json = response.json()
        token = auth_response_json.get("token")
        if token:
            logger.info("Successfully obtained Paymob authentication token.")  # Log success
            return token
        else:
            logger.error("Authentication token not found in Paymob response.")  # Log token missing error
            return None  # Or raise an exception
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during Paymob authentication: {e}")  # Log network error
        return None  # Or raise an exception
    except Exception as e:
        logger.error(f"Error during Paymob authentication: {e}")  # Log general error
        return None  # Or raise an exception


def create_paymob_order(amount, currency):
    paymob_api_endpoint_url = "https://accept.paymob.com/api/ecommerce/orders"

    token = get_paymob_auth_token()  # Get the auth token
    if not token:  # Check if token was obtained successfully
        return {"error": "Failed to obtain Paymob authentication token"}  # Return error if auth fails

    headers = {
        "Authorization": f"Bearer {token}",  # Use "Bearer" + token in header
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
        },
        "payment_methods": ["card"]  # Specify payment method as "card"
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
    paymob_api_endpoint_url = "https://accept.paymob.com/api/acceptance/payment_keys"  

    token = get_paymob_auth_token()  # Get the auth token
    if not token:  # Check if token was obtained successfully
        return {"error": "Failed to obtain Paymob authentication token"}  # Return error if auth fails

    headers = {
        "Authorization": f"Bearer {token}",  # Use "Bearer" + token in header
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
