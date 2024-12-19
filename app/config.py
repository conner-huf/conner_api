import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  BASE_URL: str = os.getenv("BASE_URL", "http://localhost:8000")

config = Config()