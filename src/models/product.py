from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    name: str
    target_price: float
    keywords: List[str]