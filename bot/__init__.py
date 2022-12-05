from os import environ
from pyrogram.client import Client

api_id = str(environ.get("API_ID"))
api_hash = str(environ.get("API_HASH"))
bot_token = str(environ.get("BOT_TOKEN"))

app = Client("kaizen", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
