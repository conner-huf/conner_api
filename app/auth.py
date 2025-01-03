from fastapi import Depends
from fastapi.security import OAuth2AuthorizationCodeBearer
from google.auth.transport.requests import Request
from google.oauth2 import id_token
import requests

# Define OAuth2 configuration for Google
GOOGLE_CLIENT_ID = "your_google_client_id"
GOOGLE_CLIENT_SECRET = "your_google_client_secret"
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

oauth2_scheme_google = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://accounts.google.com/o/oauth2/auth",
    tokenUrl="https://oauth2.googleapis.com/token",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET
)

@app.get("/login/google")
async def login_google():
    return {"authorization_url": oauth2_scheme_google.authorizationUrl}

@app.get("/auth/google/callback")
async def auth_google_callback(token: str = Depends(oauth2_scheme_google)):
    try:
        # Verify and decode the token
        idinfo = id_token.verify_oauth2_token(token, Request(), GOOGLE_CLIENT_ID)
        
        # Check if the user exists in your database
        email = idinfo.get("email")
        if email not in fake_users_db:
            # Register the user if they don't exist
            fake_users_db[email] = {"email": email, "hashed_password": ""}
        
        # Create JWT token for the user
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": email}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid Google token")
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