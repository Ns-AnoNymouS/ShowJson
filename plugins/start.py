"""
Telegram ShowJson Bot

This script contains the handler for the /start command.
"""

import logging
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from config import OWNER_ID

logger = logging.getLogger(__name__)


@Client.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    """
    Handle the /start command. Sends a welcome message with information about the bot
    and the owner's contact.

    Args:
        client (Client): The pyrogram Client.
        message (Message): The incoming message.
    """
    try:
        owner = await client.get_users(int(OWNER_ID))
        owner_username = owner.username if owner.username else "The_proGrammerr"

        # Start text
        text = f"""Hello {message.from_user.mention},

💡 **Welcome to the Telegram ShowJson Bot!**

`Easily retrieve the JSON data for your text messages, media, and more.`

**👲 Maintained By:** {owner.mention}
"""

        # Buttons
        buttons = [
            [
                InlineKeyboardButton(
                    "Meet the Creator 👨‍✈️", url=f"https://t.me/{owner_username}"
                ),
                InlineKeyboardButton(
                    "Source Code 📝", url="https://github.com/Ns-Bots/ShowJson"
                ),
            ],
            [
                InlineKeyboardButton(
                    "Help & Support ❓", url="https://t.me/Ns_AnoNymouS"
                )
            ],
        ]
        await message.reply(
            text=text, quote=True, reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as e:  # pylint: disable = broad-exception-caught
        logger.exception("An error occurred in the start handler: %s", str(e))
