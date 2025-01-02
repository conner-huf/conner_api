from motor.motor_asyncio import AsyncIOMotorClient
from app.config import config

client = AsyncIOMotorClient(config.MONGODB_URI)
resume_db = client.resumeDB
red_ribbon_db = client.redRibbon