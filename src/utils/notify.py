import aiohttp
import os
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

async def send_discord_alert(message: str):
    webhook = os.getenv("DISCORD_WEBHOOK")
    if not webhook:
        logger.warning("No Discord webhook set!")
        return
    
    async with aiohttp.ClientSession() as session:
        try:
            await session.post(webhook, json={"content": message})
        except Exception as e:
            logger.error(f"Discord alert failed: {e}")