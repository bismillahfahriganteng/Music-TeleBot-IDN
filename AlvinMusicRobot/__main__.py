import requests
from pyrogram import Client as Bot

from AlvinMusicRobot.config import API_HASH
from AlvinMusicRobot.config import API_ID
from AlvinMusicRobot.config import BG_IMAGE
from AlvinMusicRobot.config import BOT_TOKEN
from AlvinMusicRobot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="AlvinMusicRobot.modules"),
)

bot.start()
run()
