"""
Telegram ShowJson Bot

This script initializes and runs the Telegram bot using Pyrogram.
It loads configuration settings and sets up logging for debugging and monitoring.
"""

import logging
import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

async def main():
    """
    Main function to initialize and run the Telegram bot.
    """
    # Create and configure the Client
    app = Client(
        "ShowJson",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins={"root": "plugins"},
        workers=100,
    )

    # Run the bot
    await app.start()
    print(f"Bot started at: @{app.me.username}")
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
