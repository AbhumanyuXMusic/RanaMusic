# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks Β© @Dr_Asad_Ali Β© Rocks
# Owner Asad + Harshit
# πΰΌ _π‘πΎΒ Cβ€ππ’_ΤΉΥΤΉΤΊ ΰΌπ΅π° γUsα΄Κ_α΄Ιͺα΄α΄γ

import logging
from config import BOT_USERNAME
from rocksdriver.filters import command, other_filters
from pyrogram import Client
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from youtube_search import YoutubeSearch

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(command(["search", f"search@{BOT_USERNAME}"]))
async def ytsearch(_, message: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "π Close", callback_data="cls",
                )
            ]
        ]
    )

    try:
        if len(message.command) < 2:
            await message.reply_text("/search **needs an argument !**")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("π **Searching...**")
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"π· **Name:** __{results[i]['title']}__\n"
            text += f"β± **Duration:** `{results[i]['duration']}`\n"
            text += f"π **Views:** `{results[i]['views']}`\n"
            text += f"π£ **Channel:** {results[i]['channel']}\n"
            text += f"π: https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, reply_markup=keyboard, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))

# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.