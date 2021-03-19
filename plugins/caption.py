from pyrogram import (
    Client,
    filters
)

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from vars import var

USERNAME="GENRATED BY @MORAGCODES"

if var.CAPTION_MESSAGE is not None:
    START = var.CAPTION_MESSAGE
else:
    START = USERNAME


@Client.on_message(filters.caption & filters.private)
async def matrix(client, message):
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
                                     text="Bot Captions✍️",
                                     callback_data=f"add-{msg}")]])
                             )


@Client.on_callback_query()
async def cb(client, call):
    r = call.data
    msgid = int(r.split("-")[1])
    chat = call.message.chat.id
    if r.startswith("yes"):
        await call.message.delete()
        await call.message._client.copy_message(chat, chat, msgid)
    if r.startswith("no"):
        await call.message.delete()
        await call.message._client.copy_message(chat, chat, msgid,
                                                caption="")
    if r.startswith("add"):
       await call.message.delete()
       await call.message._client.copy_message(chat, chat, msgid,
                                                caption=START)
                                                
                                                
                                                
