import shutil
import time
import pytest
from routes.Routes import Routes
from utils.ConfigReader import ReadConfig
import logging
import os
import requests


# LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs", "test_logging.log"))
# Create path for log file: ../logs/test_logging.log
LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../logs/test_logging.log"))
# Create logs folder if it does not exist
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
# Create logger object with name "api_logger"
logger = logging.getLogger("api_logger")
# Set logging level (DEBUG = log everything)
logger.setLevel(logging.DEBUG)

# Prevent adding multiple handlers again and again
if not logger.handlers:
    # FileHandler → logs will be saved in a file
    file_handler = logging.FileHandler(LOG_FILE, mode="a")
    # Log format → time | level | message
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    # Apply format to file handler
    file_handler.setFormatter(formatter)
    # Attach handler to logger
    logger.addHandler(file_handler)

def log_request_response(response: requests.Response):
    req = response.request  # Get original request object
    # Log request method and URL
    logger.info(f"REQUEST: {req.method} {req.url}")

    # Log request headers
    logger.info(f"Request Headers: {req.headers}")
    # Log request body if present
    if req.body:
        logger.info(f"Request Body: {req.body}")

    # Log response status code
    logger.info(f"RESPONSE Status: {response.status_code}")

    # Log response headers
    logger.info(f"Response Headers: {response.headers}")

    # Try to log response as JSON
    try:
        logger.info(f"Response Body: {response.json()}")
    except Exception:
        # If response is not JSON → log as text
        logger.info(f"Response Body: {response.text}")



@pytest.fixture(scope= "class",autouse=True)
def setup():
    # base_url = Routes.BASE_URL
    # config_reader= ReadConfig
    # Initialize logging after cleanup
    # report_dir = "reports"
    #
    # if os.path.exists(report_dir):
    #     shutil.rmtree(report_dir)
    #
    # os.makedirs(report_dir, exist_ok=True)
    #
    # # Save original request method
    original_request = requests.Session.request

    # Create custom request function
    def custom_request(self, method, url, **kwargs):
        # Call original request
        response = original_request(self, method, url, **kwargs)

        # Log request and response
        log_request_response(response)

        return response

    # Override requests.Session.request with custom function
    requests.Session.request = custom_request


    yield {"base_url":Routes.BASE_URL, "config_reader":ReadConfig}

