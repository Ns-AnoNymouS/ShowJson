"""
Configuration Module

This module loads environment variables
and sets up the necessary configuration for the Telegram bot.
"""

from os import getenv
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve API_ID from environment variables and convert to integer
try:
    API_ID = int(getenv("API_ID"))
except (TypeError, ValueError) as exe:
    raise ValueError(
        "API_ID environment variable must be set and must be an integer"
    ) from exe

# Retrieve API_HASH from environment variables
API_HASH = getenv("API_HASH")
if not API_HASH:
    raise ValueError("API_HASH environment variable not set")

# Retrieve BOT_TOKEN from environment variables, with an empty string as a default fallback
BOT_TOKEN = getenv("BOT_TOKEN", "")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set")

# Retrieve OWNER_ID from environment variables and convert to integer
try:
    OWNER_ID = int(getenv("OWNER_ID"))
except (TypeError, ValueError) as exe:
    raise ValueError(
        "OWNER_ID environment variable must be set and must be an integer"
    ) from exe
