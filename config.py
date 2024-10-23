import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    GOOGLE_CLIENT_ID = os.getenv('CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
    GOOGLE_REDIRECT_URI = os.getenv('REDIRECT_URI')