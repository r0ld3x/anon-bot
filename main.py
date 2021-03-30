import logging
from pyrogram import Client
from vars import var

logging.basicConfig(level=logging.INFO)

api_id=var.API_ID
api_hash=var.API_HASH
bot_token=var.BOT_TOKEN

roldex = Client('anon-bot',
                  api_id="1667849",
                  api_hash="b719710209932bff18219f4064e92388",
                  bot_token="1771171629:AAGhmkT9XMzt6oLnLugzJm5tZKErNM-FnhY",                
                  plugins=dict(root="plugins"))                            
roldex.run()
