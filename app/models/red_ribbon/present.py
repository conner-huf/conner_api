from typing import Optional
from pydantic import BaseModel

class Present(BaseModel):
    title: str
    price: float
    date_requested: str
    is_purchased: bool
    date_purchased: Optional[str]
    url: str