from aiohttp_proxy import ProxyConnector
from typing import List, Optional
from pathlib import Path
import random

class ProxyManager:
    def __init__(self, proxy_file: str = "config/proxies.txt"):
        self.proxies = self._load_proxies(proxy_file)
    
    def _load_proxies(self, proxy_file: str) -> List[str]:
        if not Path(proxy_file).exists():
            return []
        with open(proxy_file) as f:
            return [line.strip() for line in f if line.strip()]
    
    def get_random_connector(self) -> Optional[ProxyConnector]:
        if not self.proxies:
            return None
        proxy_url = random.choice(self.proxies)
        return ProxyConnector.from_url(proxy_url)

# Singleton instance
proxy_manager = ProxyManager()