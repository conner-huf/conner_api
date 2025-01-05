from fastapi.encoders import jsonable_encoder
import requests
from bson import ObjectId

from app.config import config
from app.data.db import red_ribbon_db as db
from app.models.red_ribbon.user import User

class RedRibbonService:
    users = db.Users
    
    @staticmethod
    async def get_user_wishlist(user_id: str) -> dict:
        try:
            object_id = ObjectId(user_id)

            user = await RedRibbonService.users.find_one({"_id": object_id})
            if user:
                user_model = User(**user)
                return jsonable_encoder(user_model.wishlist)
            else:
                return {"error": f"user {user_id} not found"}
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    async def get_user_info(user_id: str) -> dict:
        try:
            object_id = ObjectId(user_id)

            user = await RedRibbonService.users.find_one({"_id": object_id})
            if user:
                user_model = User(**user)
                return jsonable_encoder(user_model)
            else:
                return {"error": f"user {user_id} not found"}
        except Exception as e:
            return {"error": str(e)}
        
    # TODO: Implement a method for adding an item to a user's wish list

    # TODO: Implement a method for deleting an item from a user's wish list

    # TODO: Implement a method for updating an item on a user's wish list

    # TODO: Implement a method for creating a new gift group

    # TODO: Implement a method for fetching all members in a gift group

    # TODO: Implement a method for adding an existing user to a gift group

    # TODO: Implement a method for deleting an existing user from a gift group
