
from typing import List
from pydantic import BaseModel
from datetime import date

from app.models.red_ribbon.user import User

class GiftGroup(BaseModel):
    title: str
    participants: List[User]
    price_ceiling: float
    date_of_exchange: date
    