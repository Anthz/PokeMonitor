import aiohttp
from aiohttp_proxy import ProxyConnector
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from typing import List, Optional
from ..models.listing import Listing
from ..utils.proxy import proxy_manager
from ..utils.logger import logger

class EbayScraper:
    def __init__(self):
        self.ua = UserAgent()
    
    async def fetch_listings(self, product_name: str) -> List[Listing]:
        url = f"https://www.ebay.co.uk/sch/i.html?_nkw={product_name.replace(' ', '+')}"
        headers = {"User-Agent": self.ua.random}
        connector = proxy_manager.get_random_connector()  # Random proxy
        
        try:
            async with aiohttp.ClientSession(
                connector=connector,
                headers=headers
            ) as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        logger.warning(f"Proxy failed. Status: {response.status}")
                        return await self.fetch_listings(product_name)  # Retry
                    
                    html = await response.text()
                    soup = BeautifulSoup(html, "html.parser")
                    return self._parse_listings(soup)
        
        except Exception as e:
            logger.error(f"Request failed: {e}")
            return []

    def _parse_listings(self, soup: BeautifulSoup) -> List[Listing]:
        listings = []
        for item in soup.select("li.s-item"):
            title = item.select_one("span[role='heading']").text.strip()
            price_text = item.select_one("span.s-item__price").text.strip()
            price = float(price_text.replace("£", "").replace(",", ""))
            url = item.select_one("a.s-item__link")["href"].split("?")[0]
            
            listings.append(Listing(title=title, price=price, url=url))
        return listings