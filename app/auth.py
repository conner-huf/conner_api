from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer
from google.auth.transport.requests import Request
from google.oauth2 import id_token
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
import requests

from app.config import config
from app.models.red_ribbon.user import User
from app.data.db import red_ribbon_db as db

client_id = config.GOOGLE_CLIENT_ID
client_secret = config.GOOGLE_CLIENT_SECRET
discovery_url = config.GOOGLE_DISCOVERY_URL

oauth2_scheme_google = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://accounts.google.com/o/oauth2/auth",
    tokenUrl="https://oauth2.googleapis.com/token",
    client_id=client_id,
    client_secret=client_secret
)

class Token(BaseModel):
    access_token: str
    token_type: str

async def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(datetime.timezone.utc) + expires_delta
    else:
        expire = datetime.now(datetime.timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt

router = APIRouter()

@router.post("/login/google")
async def login_google():
    return {"authorization_url": oauth2_scheme_google.authorizationUrl}

@router.post("/auth/google_callback", response_model=Token)
async def auth_google_callback(token: str = Depends(oauth2_scheme_google)):
    try:
        # Verify and decode the token
        idinfo = id_token.verify_oauth2_token(token, Request(), client_id)
        
        # Extract user information
        email = idinfo.get("email")
        name = idinfo.get("name")
        
        # Check if the user exists in your database
        user = await db.Users.find_one({"email": email})
        if not user:
            # Register the user if they don't exist
            user = User(email=email, name=name)
            await db.Users.insert_one(user.dict())
        
        # Create JWT token for the user
        access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = await create_access_token(data={"sub": email}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid Google token")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    '''
    # TODO: 

    Create Google Cloud Project:

    Create a project in the Google Cloud Console to manage your OAuth2 credentials.
    OAuth Consent Screen:

    Configure the consent screen that users will see when they authorize your app.
    OAuth2 Credentials:

    Create OAuth2 credentials and get your client ID and client secret.
    FastAPI Integration:

    Use the google-auth and google-auth-oauthlib libraries to handle Google OAuth2.
    The /login/google endpoint redirects users to the Google OAuth2 consent screen.
    The /auth/google/callback endpoint handles the callback from Google, exchanges the authorization code for an ID token, and verifies it.
    After verification, the user's email is extracted and used to either log in or register the user.

    '''
    # TODO: Test this auth flow with frontend before working 'add user' steps