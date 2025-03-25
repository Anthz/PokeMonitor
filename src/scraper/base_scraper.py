from abc import ABC, abstractmethod
from typing import List
from ..models.listing import Listing

class BaseScraper(ABC):
    @abstractmethod
    def fetch_listings(self, product_name: str) -> List[Listing]:
        pass