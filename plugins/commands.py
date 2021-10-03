import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command('start'))
async def start(c, m):
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'Tellybots_4u'

    # start text
    text = f"""Hey! {m.from_user.mention(style='md')},

💡  I am Telegram ShowJson Bot

Send Msg by own or forward msg from channel to get json details.

Developed by: {owner.mention(style='md')}
"""

    # Buttons
    buttons = [
        [
            InlineKeyboardButton('Developer', url=f"https://t.me/{owner_username}")
        ]
[
            InlineKeyboardButton('Support Group', url=f"https://tellybots_support")
        ]
]
    await m.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )



@Client.on_message(filters.private & filters.incoming)
async def show_json(c, m):
    text = f'{m}'
    if len(text) <= 4096:
        await m.reply_text(text)
    else:
        with open(f'Your json file {m.from_user.first_name}.json', 'w') as f:
            f.write(text)
        await m.reply_document(f'Your json file {m.from_user.first_name}.json', True)
        os.remove(f'Your json file {m.from_user.first_name}.json')

@Client.on_inline_query()
async def inline_json(c, m):
    text = f'{m}'
    if len(text) <= 4096:
        await c.send_message(chat_id=m.from_user.id, text=text)
    else:
        with open(f'Your json file {m.from_user.first_name}.json', 'w') as f:
            f.write(text)
        await c.send_document(chat_id=m.from_user.id, file_name=f'Your json file {m.from_user.first_name}.json')
        os.remove(f'Your json file {m.from_user.first_name}.json')

    await m.answer(
        results=[],
        switch_pm_text=f"Hi I sent Json in pm",
        switch_pm_parameter="start",
    )
