from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Dict, Any
import aiohttp

@dataclass
class ScrapeResult:
    success: bool
    data: Optional[Dict[str, Any]]
    error: Optional[str]

class BaseScraper(ABC):
    def __init__(self):
        self._session = None
        self.config = {}

    @property
    @abstractmethod
    def required_fields(self) -> Dict[str, Dict]:
        return {
            "base_url": {
                "type": "str",
                "default": "",
                "help": "Root URL for the target site"
            }
        }

    async def initialize(self):
        """Initialize resources"""
        self._session = aiohttp.ClientSession()

    async def cleanup(self):
        """Release resources"""
        if self._session:
            await self._session.close()

    @abstractmethod
    async def scrape(self, product_query: str) -> ScrapeResult:
        pass

    async def _request(self, url: str) -> ScrapeResult:
        try:
            if not self._session:
                await self.initialize()
            async with self._session.get(url) as response:
                return ScrapeResult(
                    success=True,
                    data=await response.text(),
                    error=None
                )
        except Exception as e:
            return ScrapeResult(
                success=False,
                data=None,
                error=str(e)
            )