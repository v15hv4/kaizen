from os import environ

import openai

from bot import app
from pyrogram import enums, filters


# respond using a GPT-3 model
@app.on_message(filters.mentioned)
async def gpt3chat(client, message):
    query = " ".join(message.text.split()[1:])
    prompt = f"Q: {query}\nA: "

    openai.api_key = str(environ.get("OPENAI_TOKEN"))

    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    await message.reply(completion.choices[0]["text"].strip())
