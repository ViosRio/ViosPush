
#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
import os
from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import CallbackQuery
from config import *
import requests
from pyrogram import filters

import os,sys,re,requests
import asyncio,time
from random import choice
from datetime import datetime
import logging

FORMAT = "[LEGEND-MUKESH] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
Mukesh = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
๏ 𝗠𝗲𝗿𝗵𝗮𝗯𝗮 🌹

MERHABA KANALDA REKLAM VERMEYEMİ İHTİYAÇ DUYDUN OZAMAN DOĞRU KAPI ÇALDIN
"""
xa = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
SOURCE = xa
SOURCE_TEXT = f"""
๏ ʜᴇʏ,
"""


x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(text="sᴀʜɪᴘ", url=f"https://t.me/{OWNER_USERNAME}")
    ],
    [
        InlineKeyboardButton(
            text="ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʏᴀʀᴅıᴍ & ᴋᴏᴍᴜᴛʟᴀʀ ", callback_data="HELP"),
        InlineKeyboardButton(text="BONUS BAKİYE ", callback_data="BALANCE"),
        InlineKeyboardButton(text="REKLAM VER ", callback_data="ADS"),
    ],
]
X = [
    [
        InlineKeyboardButton(text=" ᴅᴇsᴛᴇᴋ ", url=f"https://t.me/{SUPPORT_GRP}"),
    ]
    ]
    
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="ᴅᴇsᴛᴇᴋ", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('sᴏᴜʀᴄᴇ', url=f"{SOURCE}")]])
HELP_READ = "**➻ 𝗞𝘂𝗹𝗹𝗮𝗻ı𝗺 :**  \n\n/bul 𝗬𝗼𝘂𝘁𝘂𝗯𝗲 𝗠𝗽𝟯 𝗜𝗻𝗱𝗶𝗿𝗺𝗲 𝗢𝘇𝗲𝗹𝗹𝗶𝗴𝗶\n\n/ping 𝗕𝗼𝘁𝘂𝗻 𝗦𝗮ğ𝗹ı𝗸 𝗦𝗼𝗿𝘂𝗻𝗹𝗮𝗿ı𝗻ı 𝗧𝗲𝘀𝘁 𝗘𝗱𝗶𝗻\n\nʙᴏᴛ ᴠᴇʀsɪᴏɴ ᴠ2.1"
HELP_BACK = [
     [
           InlineKeyboardButton(text="ᴋᴀʏɴᴀᴋ ", url=f"https://github.com/ViosRio/ViosPush"),
           
     ],
    [
           InlineKeyboardButton(text="⬅️ ", callback_data="HELP_BACK"),
    ],
]

  
#         start
@Mukesh.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("✦ Yᴜ̈ᴋʟᴇɴɪʏᴏʀ..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    except Exception as y:
        await m.reply(y)
#  callback 
@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@Mukesh.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_photo(START_IMG,
                        caption=HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@Mukesh.on_message(filters.command(['source', 'repo'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@Mukesh.on_message(filters.command(["ping","alive"], prefixes=["+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "Bekleyiniz.."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("✦ Yᴜ̈ᴋʟᴇɴɪʏᴏʀ..")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"ʜᴇʏ !!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) ɪ̇ʟᴇᴛɪşɪᴍ ᴠᴇ öɴᴇʀɪ \n➥ `{ms}` ms\n\n**🌹 || [sᴀʜɪᴘ](https://t.me/{OWNER_USERNAME})||",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

# REKLAM


        
        
            
        

s = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()

if SOURCE != s:
    print("So sad, you have changed source, change it back to ` https://github.com/Noob-mukesh/Chatgpt-bot `  else I won't work")
    sys.exit(1)  


if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        Mukesh.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN  @MR_SUKKUN
GIVE STAR TO THE REPO 
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    Mukesh.stop()
    print("Bot stopped. Bye !")
#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
