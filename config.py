import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Itz_VeNom_xD")
ALIVE_NAME = getenv("ALIVE_NAME", "Venom_Hai_Hum")
BOT_USERNAME = getenv("BOT_USERNAME", "QueenAlishaRobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Queen_Alisha")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AlishaSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ABOUTABHI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/763dedb3000b7f03168ea.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/b37a0590fa12427e6cf0a.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/b37a0590fa12427e6cf0a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/b37a0590fa12427e6cf0a.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/b37a0590fa12427e6cf0a.jpg")
