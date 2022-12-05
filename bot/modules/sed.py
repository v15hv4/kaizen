import re

from bot import app
from pyrogram import filters

# perform regex substitution on the message the command was a reply to
@app.on_message(filters.regex("^s/"))
async def sed(client, message):
    if not message.reply_to_message_id:
        message.reply("Do u even sed m8?")

    query = message.text + "/"
    target = message.reply_to_message.text

    _, pattern, repl, options, *_ = re.split(r"(?<![^\\]\\)/", query)
    result = re.sub(
        pattern, re.sub(r"\\/", "/", repl), target, count="g" not in options
    )

    await message.reply_to_message.reply(result)
