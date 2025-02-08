import os
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv(".env.local")

GROCLAKE_API_KEY = os.getenv("GROCLAKE_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
