from pydantic import BaseModel

class Listing(BaseModel):
    title: str
    price: float
    url: str
    site: str = "eBay UK"