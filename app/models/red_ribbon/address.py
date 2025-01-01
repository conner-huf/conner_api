from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    street_address: str
    zip_code: str
    