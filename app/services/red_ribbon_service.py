import requests
from bson import ObjectId
from app.config import config
from app.data.db import red_ribbon_db as db

class RedRibbonService:
    
    @staticmethod
    async def get_user_wishlist(user_id: str) -> dict:
        try:
            object_id = ObjectId(user_id)

            users = db.Users
            user = await users.find_one({"_id": object_id})
            if user:
                return user.get("wishlist", [])
            else:
                return {"error": f"user {user_id} not found"}
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    async def get_user_info(user_id: str) -> dict:
        try:
            object_id = ObjectId(user_id)

            users = db.Users
            user = await users.find_one({"_id": object_id})
            if user:
                user["_id"] = str(user["_id"])
                return user
            else:
                return {"error": f"user {user_id} not found"}
        except Exception as e:
            return {"error": str(e)}