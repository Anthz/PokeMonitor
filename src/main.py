from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.orm import Session
from src.scraper.ebay_scraper import EbayScraper
from src.models.product import Product
from src.models.database import ListingHistory, engine
from src.utils.logger import logger
from src.utils.notify import send_discord_alert
import yaml
import hashlib

async def load_products() -> list[Product]:
    with open("config/products.yaml") as f:
        return [Product(**data) for data in yaml.safe_load(f)]

async def check_products():
    scraper = EbayScraper()
    products = await load_products()
    
    with Session(engine) as session:
        for product in products:
            listings = await scraper.fetch_listings(product.name)
            for listing in listings:
                # Save to database
                listing_id = hashlib.md5(listing.url.encode()).hexdigest()
                db_entry = ListingHistory(
                    id=listing_id,
                    title=listing.title,
                    price=listing.price,
                    url=listing.url
                )
                session.merge(db_entry)  # Upsert operation
                session.commit()
                
                # Alert if price is low
                if listing.price <= product.target_price:
                    alert = f"🚨 Deal: {listing.title} (£{listing.price})\n{listing.url}"
                    logger.success(alert)
                    await send_discord_alert(alert)

if __name__ == "__main__":
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_products, "interval", minutes=5)
    scheduler.start()
    
    try:
        import asyncio
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        logger.info("Bot stopped")