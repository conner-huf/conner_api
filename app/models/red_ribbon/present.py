from pydantic import BaseModel
from datetime import date

class Present(BaseModel):
    title: str
    price: float
    date_requested: date
    is_purchased: bool
    url: str