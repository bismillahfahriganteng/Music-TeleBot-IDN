import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CH = getenv("UPDATES_CHANNEL", "alvin_image_editor")
UPDATES_MODE = getenv("UPDATES_MODE", "Updates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/eb88ad83fbaabbc57cd4d.jpg")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
ASSISSTANT_MODE = getenv("ASSISSTANT_MODE", "Assisstant")
SUPPORT_GRP = getenv("SUPPORT_GROUP", "alvin_image_editor")
SUPPORT_MODE = getenv("SUPPORT_MODE", "Support")
PROJECT_NAME = getenv("PROJECT_NAME", "Alvin Music")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/bismillahfahriganteng/Music-TeleBot-IDN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
CREATOR_NAME = getenv("CREATOR_NAME", "Muhammad Fahri")
CREATOR_USERNAME = getenv("CREATOR_USERNAME", "alvin_junior")
OWNER_MODE = getenv("OWNER_MODE", "Creator")
