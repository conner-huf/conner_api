from pydantic import BaseModel
from app.models.red_ribbon.present import Present
from app.models.red_ribbon.user import User
from typing import List

class Participant(BaseModel):
    user_reference: User
    giving_gift_to: User
    receiving_gift_from: User
    