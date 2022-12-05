import random
import requests

from bot import app
from pyrogram import enums, filters


@app.on_message(filters.command("dadjoke"))
async def dadjoke(client, message):
    response = requests.get(
        "https://www.reddit.com/r/dadjokes.json",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
        },
    )
    response = response.json()

    pick = random.randint(0, 25)
    head = response["data"]["children"][pick]["data"]["title"]
    body = response["data"]["children"][pick]["data"]["selftext"]

    await message.reply(f"*{head}*\n{body}", parse_mode=enums.ParseMode.MARKDOWN)
