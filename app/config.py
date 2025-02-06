import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  BASE_URL: str = os.getenv("BASE_URL", "http://localhost:8000")
  MONGODB_URI: str = os.getenv("MONGODB_URI", "http://localhost:27017")
  SPOTIFY_CLIENT_ID: str = os.getenv("SPOTIFY_CLIENT_ID")
  SPOTIFY_CLIENT_SECRET: str = os.getenv("SPOTIFY_CLIENT_SECRET")
  TICKETMASTER_API_KEY: str = os.getenv("TICKETMASTER_API_KEY")
  TICKETMASTER_SECRET: str = os.getenv("TICKETMASTER_SECRET")
  GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID")
  GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET")
  GOOGLE_DISCOVERY_URL: str = os.getenv("https://accounts.google.com/.well-known/openid-configuration")
  SECRET_KEY: str = os.getenv("SECRET_KEY", "strong secret key for jwt")
  
  ALGORITHM = "HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES = 30


config = Config()