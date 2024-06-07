"""
Telegram ShowJson Bot Handlers

This script contains the handlers for private messages and inline queries.
It converts incoming messages to their JSON representation and replies with
the JSON data.
"""

import os
import logging

from pyrogram import Client, filters
from pyrogram.types import Message, InlineQuery
from pyrogram.errors import UserIsBlocked, PeerIdInvalid

logger = logging.getLogger(__name__)


@Client.on_message(filters.private & filters.incoming & ~filters.command("start"))
async def show_json(_: Client, message: Message):
    """
    Handle incoming private messages (excluding the /start command) and reply
    with the JSON representation of the message.

    Args:
        client (Client): The pyrogram client.
        message (Message): The incoming message.
    """
    try:
        text = f"`{message}`"
        if len(text) <= 4096:
            # If the JSON text is small enough, reply directly with the JSON text
            await message.reply(text)
        else:
            # If the JSON text is too large, write it to a file and send the file
            file_name = f"Your_json_file_{message.from_user.first_name}.json"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(text)
            await message.reply_document(file_name, caption="Here is your JSON file.")
            os.remove(file_name)
    except Exception as e:  # pylint: disable = broad-exception-caught
        logger.exception("An error occurred in the show_json handler: %s", str(e))


@Client.on_inline_query()
async def inline_json(client: Client, inlinequery: InlineQuery):
    """
    Handle incoming inline queries and reply with the JSON representation of the query.

    Args:
        client (Client): The pyrogram client.
        inlinequery (InlineQuery): The incoming inline query.
    """
    try:
        try:
            switch_pm_text = "Hey i sent the json in PM 😉"
            text = f"`{inlinequery}`"
            if len(text) <= 4096:
                # If the JSON text is small enough, send a private message with the JSON text
                await client.send_message(chat_id=inlinequery.from_user.id, text=text)
            else:
                # If the JSON text is too large, write it to a file and send the file
                file_name = f"Your_json_file_{inlinequery.from_user.first_name}.json"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(text)
                await client.send_document(
                    chat_id=inlinequery.from_user.id,
                    document=file_name,
                    caption="Here is your JSON file.",
                )
                os.remove(file_name)
        except UserIsBlocked:
            switch_pm_text = "You have Blocked the bot,Unblock it "
        except PeerIdInvalid:
            switch_pm_text = "Please start the bot once in pm and try again"

        # Answer the inline query with a prompt to check their private messages
        await inlinequery.answer(
            results=[],
            switch_pm_text=switch_pm_text,
            switch_pm_parameter="start",
        )
    except Exception as e:  # pylint: disable = broad-exception-caught
        logger.exception("An error occurred in the inline_json handler: %s", str(e))
