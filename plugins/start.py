from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME as bn
from helpers.filters import other_filters2
from time import time
from datetime import datetime
from helpers.decorators import authorized_users_only
from config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**مرحبا, انا {bn} 🎀
يسمح لك بتشغيل الموسيقى والفيديو في مجموعات من خلال محادثات الفيديو الجديدة في التلي [𝑆𝐼𝐸𝑆𝑇𝐴_𝑋_𝑀𝑈𝑆𝐼𝐶](https://t.me/MR_MUSlC_Bot).
⋆ قم بإضافة البوت اللي مجموعتك لكي تبدا الحفله..😺♥️**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الاوامر🧰", url="https://telegra.ph/%F0%9D%90%82%F0%9D%90%A8%F0%9D%90%A6%F0%9D%90%A6%F0%9D%90%9A%F0%9D%90%A7%F0%9D%90%9D%F0%9D%90%AC-%F0%9D%90%85%F0%9D%90%A8%F0%9D%90%AB-%F0%9D%91%BA%F0%9D%91%B0%F0%9D%91%AC%F0%9D%91%BA%F0%9D%91%BB%F0%9D%91%A8-%F0%9D%91%BF-%F0%9D%90%8C%F0%9D%90%AE%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%9C-%F0%9D%90%81%F0%9D%90%A8%F0%9D%90%AD-03-13")
                  ],[
                    InlineKeyboardButton(
                       " قناة البوت..🙂♥👿", url="https://t.me/vod_ika0"
                    ),
                    InlineKeyboardButton(
                        "مبرمج السورس يبني..📚", url="https://t.me/v_o_d_i_k_a"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕ اضف البوت الي مجموعتك..🙂♥➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
