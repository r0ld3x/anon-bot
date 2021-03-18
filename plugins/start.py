from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from vars import vars
from pyrogram import *
START_MSG = """
Hi, I am **Ark Anonymous File Sender Bot.**\n
Just Send me Any Files I will Hide Owner And  Make It anonymous
YOU CAN ALSO CLONE ME FROM :-

"""

if var.START_MESSAGE is not None:
  START = var.START_MESSAGE
  else:
    START = START_MSG

REPLY_MARKUP = InlineKeyboardMarkup([
  [InlineKeyboardButton("SUPPORT GROUP",
  url="t.me/arkcodes")],
  [InlineKeyboardButton("DEVELOPER",
  url="t.me/r0ld3x")]]

@client.on_message(filters.command('start') & filters.private)
async def start(client, message):
  await message.reply_text(START, reply_markup=REPLY_MARKUP)


@Client.on_message(filters.caption & filters.private)
async def addorno(client, message):
    msg = message.message_id
    await message.reply_text('Do You Need Caption?',
                             quote=True,
                             reply_markup=InlineKeyboardMarkup(
                               [[InlineKeyboardButton(
                                   text="Yes ✅",
                                   callback_data=f"yes-{msg}"),
                                   InlineKeyboardButton(
                                     text="No ❌",
                                     callback_data=f"no-{msg}"),
                                 InlineKeyboardButton(
                                     text="Add Bot Captions✍️",
                                     callback_data=f"add-{msg}")]])
                             )

#MADE BY ROLDEX
@Client.on_message(filters.private & ~filters.caption & ~filters.command("start"))


async def copy(client, message):
  chat = message.chat.id
  await message.copy(chat)





@Client.on_callback_query()
async def cb(client, call):
    k = call.data
    msgid = int(k.split("-")[1])
    chat = call.message.chat.id
    if k.startswith("yes"):
        await call.message.delete()
        await call.message._client.copy_message(chat, chat, msgid)
    if k.startswith("no"):
        await call.message.delete()
        await call.message._client.copy_message(chat, chat, msgid,
                                                caption="")
     if k.startswith("add"):
       await call.message.delete()
       await call.message._client.copy_message(chat, chat, msgid,
                                                caption="@arkcodes")
                                                
TEXT="""
This Feature Not Available Yet😔. \n Tell Me If You Want This At @arkcodes
"""
@Client.on_message(filters.group & ~filters.channel)
async def leave(client, message)
await message.reply_text(TEXT)
await message.chat.leave()