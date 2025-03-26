from bs4 import BeautifulSoup
from .base_scraper import BaseScraper, ScrapeResult
from typing import List, Dict
import re

class EbayScraper(BaseScraper):
    def __init__(self):
        super().__init__()
        self.debug = None  # Initialize debug attribute

    async def scrape(self, product_query: str) -> ScrapeResult:
        self.debug.log(f"Starting search for: {product_query}", 
                     data={"query": product_query})
        
        try:
            url = self._build_search_url(product_query)
            self.debug.log(f"Built search URL: {url}")
            
            result = await self._request(url)
            if not result.success:
                self.debug.log("Request failed", 
                             level="error",
                             data={"error": result.error})
                return result
                
            parsed = self._parse_listings(result.data)
            self.debug.log(f"Found {len(parsed)} listings", 
                         data={"sample": parsed[:1] if parsed else None})
            
            return ScrapeResult(success=True, data=parsed)
            
        except Exception as e:
            self.debug.log("Scraping crashed", 
                         level="critical",
                         data={"exception": str(e)})
            return ScrapeResult(success=False, error=str(e))