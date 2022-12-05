import requests

from bot import app
from pyrogram import filters


@app.on_message(filters.text)
async def greet(client, message):
    response = requests.get("https://www.greetingsapi.com/random")
    response = response.json()

    greeting = response["greeting"]
    name = message.from_user.first_name

    await message.reply(f"{greeting}, {name}!")


app.run()
