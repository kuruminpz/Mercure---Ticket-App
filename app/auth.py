import os
from flask import redirect, session, url_for, request
from requests_oauthlib import OAuth2Session
from config import Config
import requests
from dotenv import load_dotenv

load_dotenv()

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


def get_google_provider_cfg():
    return requests.get(Config.GOOGLE_DISCOVERY_URL).json()

def get_google_oauth_session(token=None):
    google_provider_cfg = get_google_provider_cfg()

    return OAuth2Session(
        Config.GOOGLE_CLIENT_ID,
        redirect_uri=Config.GOOGLE_REDIRECT_URI,
        token=token,
        scope=["openid", "https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"]
    )

def google_login():
    google = get_google_oauth_session()
    authorization_url, state = google.authorization_url(get_google_provider_cfg()["authorization_endpoint"])
    session["oauth_state"] = state
    return redirect(authorization_url)

def google_callback():
    print(f"Client ID: {Config.GOOGLE_CLIENT_ID}")
    print(f"Client Secret: {Config.GOOGLE_CLIENT_SECRET}")

    google = get_google_oauth_session()
    token_url = get_google_provider_cfg()["token_endpoint"]
    print(f"Authorization Response URL: {request.url}")

    token = google.fetch_token(token_url, client_secret=Config.GOOGLE_CLIENT_SECRET, authorization_response=request.url)

    session["oauth_token"] = token

    userinfo_endpoint = get_google_provider_cfg()["userinfo_endpoint"]
    userinfo_response = google.get(userinfo_endpoint)

    userinfo = userinfo_response.json()
    session["userinfo"] = userinfo

    return redirect(url_for('main.dashboard'))
