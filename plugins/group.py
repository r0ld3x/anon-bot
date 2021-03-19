from pyrogram import Client, filters

TEXT="""
This Feature Not Available Yet😔. \n Tell Me If You Want This At @arkcodes
"""
@Client.on_message(filters.group & ~filters.channel)
async def leave(client, message):
await message.reply_text(TEXT)
await message.chat.leave()
