from pydantic import BaseModel
from datetime import date

class Trade(BaseModel):
    issuer_name: str
    date_published: date
    date_traded: date
    days_filed_after: int
    type: str
    size: str
    trade_url: str