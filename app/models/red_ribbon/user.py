from pydantic import BaseModel
from app.models.red_ribbon.address import Address

class User(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: str
    shipping_address: Address
