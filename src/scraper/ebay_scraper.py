from bs4 import BeautifulSoup
from .base_scraper import BaseScraper, ScrapeResult
from typing import List, Dict
import re

class EbayScraper(BaseScraper):
    @property
    def required_fields(self):
        return {
            **super().required_fields,
            "listings_selector": {
                "type": "str",
                "default": "li.s-item",
                "help": "CSS selector for product listings"
            }
        }

    async def scrape(self, product_query: str) -> ScrapeResult:
        url = f"{self.config['base_url']}/sch/i.html?_nkw={product_query}"
        result = await self._request(url)
        
        if not result.success:
            return result

        try:
            soup = BeautifulSoup(result.data, 'html.parser')
            listings = []
            
            for item in soup.select(self.config['listings_selector']):
                title_elem = item.select_one('span[role="heading"]')
                price_elem = item.select_one('span.s-item__price')
                
                if not (title_elem and price_elem):
                    continue
                
                price_text = re.sub(r'[^\d.]', '', price_elem.text)
                
                listings.append({
                    'title': title_elem.text.strip(),
                    'price': float(price_text),
                    'url': item.select_one('a.s-item__link')['href']
                })
                
            return ScrapeResult(
                success=True,
                data={'listings': listings},
                error=None
            )
        except Exception as e:
            return ScrapeResult(
                success=False,
                data=None,
                error=f"Parsing failed: {str(e)}"
            )