import requests

from pyrogram import filters

from bot import app
from bot.modules import good_stuff, sed, gpt3


# send the user a random greeting
@app.on_message(filters.regex("(?i)^(hey|hello|hi|sup|yo) kaizen"))
async def greet(client, message):
    response = requests.get("https://www.greetingsapi.com/random")
    response = response.json()

    greeting = response["greeting"]
    name = message.from_user.first_name

    await message.reply(f"{greeting}, {name}!")


app.run()
