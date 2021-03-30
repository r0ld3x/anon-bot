import logging
from pyrogram import Client
from vars import var

logging.basicConfig(level=logging.INFO)

api_id=var.API_ID
api_hash=var.API_HASH
bot_token=var.BOT_TOKEN

roldex = Client('anon-bot',
                  api_id,
                  api_hash,
                  bot_token,                
                  plugins=dict(root="plugins"))                            
roldex.run()
run()
