import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  BASE_URL: str = os.getenv("BASE_URL", "http://localhost:8000")
  MONGODB_URI: str = os.getenv("MONGODB_URI", "http://localhost:27017")

config = Config()