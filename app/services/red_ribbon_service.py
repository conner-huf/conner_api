import requests
from app.config import config

class RedRibbonService:

    @staticmethod
    async def test(user_id: int) -> dict:
        try:
            return {"message": f"gifts for user {user_id} fetched"}
        except Exception as e:
            return {"error": str(e)}