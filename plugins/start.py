from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from vars import var


START_MSG = """
Hey! This Is Me ANONYMOUS-BOT. \n
I WILL HIDE SENDER NAME, TAG AND CAPTIONS.\n JUST SEND ME ANY MEDIA AND MESSAGES.
"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("⛑️ SUPPORT ⛑️",
                          url="t.me/moragchats")],
    [InlineKeyboardButton(" 👨 DEV 👨 ",
                          url="t.me/r0ld3x")],
    [InlineKeyboardButton("📩DEPLOY",
                          url="https://github.com/r0ld3x/anon-bot")]])


@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(START,
                             reply_markup=REPLY_MARKUP)
