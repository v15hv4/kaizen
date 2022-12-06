import re
import random
import requests

from bot import app
from pyrogram import enums, filters

# forward a random (text) post from r/dadjokes
@app.on_message(filters.command("dadjoke"))
async def dadjoke(client, message):
    uri = "https://www.reddit.com/r/dadjokes.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    }

    response = requests.get(uri, headers=headers)
    response = response.json()

    pick = random.randint(0, 25)
    head = response["data"]["children"][pick]["data"]["title"]
    body = response["data"]["children"][pick]["data"]["selftext"]

    await message.reply(f"**{head}**\n{body}", parse_mode=enums.ParseMode.MARKDOWN)


# look up the definition of the target query on UrbanDictionary
@app.on_message(filters.command("define"))
async def define(client, message):
    try:
        query = " ".join(message.text.split()[1:])

        uri = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        headers = {
            "x-rapidapi-host": "mashape-community-urban-dictionary.p.rapidapi.com",
            "x-rapidapi-key": "f0e32f8badmsh0b2fa1d896283f6p1a3cc4jsnd24d74fcd0b2",
        }

        response = requests.get(uri, headers=headers, params={"term": query})
        response = response.json()

        definition = response["list"][0]
        word = definition["word"]
        link = definition["permalink"]
        desc = re.sub(r"[\[\]]", "", definition["definition"])
        exam = re.sub(r"[\[\]]", "", definition["example"])

        await message.reply(
            f"[{word}:]({link})\n\n{desc}\n\n__{exam}__",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )

    except:
        await message.reply(r"¯\_(ツ)_/¯")
