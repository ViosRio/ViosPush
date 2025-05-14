#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
import os
import json
from datetime import datetime, timedelta
from pyrogram import Client, filters, enums, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import *
import asyncio
import time
from random import choice
import logging

FORMAT = "[LEGEND-MUKESH] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Bakiye Sistemi
BALANCE_FILE = "balances.json"

class BalanceManager:
    @staticmethod
    def _load_data():
        if not os.path.exists(BALANCE_FILE):
            return {}
        with open(BALANCE_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def _save_data(data):
        with open(BALANCE_FILE, "w") as f:
            json.dump(data, f)

    @staticmethod
    def get_balance(user_id):
        data = BalanceManager._load_data()
        return data.get(str(user_id), {"balance": 0, "last_daily": None}

    @staticmethod
    def update_balance(user_id, amount):
        data = BalanceManager._load_data()
        user_data = data.get(str(user_id), {"balance": 0, "last_daily": None})
        user_data["balance"] = max(0, user_data["balance"] + amount)
        data[str(user_id)] = user_data
        BalanceManager._save_data(data)
        return user_data["balance"]

    @staticmethod
    def can_claim_daily(user_id):
        user = BalanceManager.get_balance(user_id)
        if not user["last_daily"]:
            return True
        last_claim = datetime.strptime(user["last_daily"], "%Y-%m-%d %H:%M:%S")
        return datetime.now() - last_claim > timedelta(hours=24)

StartTime = time.time()
Mukesh = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START = f"""
๏ 𝗠𝗲𝗿𝗵𝗮𝗯𝗮 🌹

{ReklamBotu} ile kolayca reklam verebilirsiniz!
Günlük {DAILY_BONUS} ücretsiz bakiye kazanın.
"""

x = ["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g = choice(x)

MAIN = [
    [
        InlineKeyboardButton(text="sᴀʜɪᴘ", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text="ʙᴀᴋɪʏᴇ ʏüᴋʟᴇ", callback_data="ADD_BALANCE")
    ],
    [
        InlineKeyboardButton(
            text="ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʏᴀʀᴅıᴍ & ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="HELP"),
        InlineKeyboardButton(text="ʙᴀᴋɪʏᴇᴍ", callback_data="MY_BALANCE"),
    ],
    [
        InlineKeyboardButton(text="ʀᴇᴋʟᴀᴍ ᴠᴇʀ", callback_data="ADS"),
    ]
]

@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
        await query.message.edit_text(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BACK),
        )
    elif query.data == "HELP_BACK":
        await query.message.edit(
            text=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    elif query.data == "MY_BALANCE":
        user_id = query.from_user.id
        user = BalanceManager.get_balance(user_id)
        await query.message.edit(
            text=f"💰 Bakiyeniz: {user['balance']} puan",
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    elif query.data == "ADD_BALANCE":
        if query.from_user.id not in SUDO:
            await query.answer("❌ Bu işlem için yetkiniz yok!", show_alert=True)
            return
        
        await query.message.edit(
            text="💳 Bakiye yükleme paneli:\n\nKullanıcı adı veya ID girin:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("İᴘᴛᴀʟ", callback_data="HELP_BACK")]
            ])
        )
        # Burada bakiye yükleme işlemleri devam edecek

# Admin bakiye ekleme komutu
@Mukesh.on_message(filters.command("addbalance") & filters.user(SUDO))
async def add_balance(client, message):
    if len(message.command) < 3:
        await message.reply("Kullanım: /addbalance [kullanıcı] [miktar]")
        return
    
    try:
        user = message.command[1]
        amount = int(message.command[2])
        
        if user.startswith("@"):
            user = user[1:]
            # Burada kullanıcı adından ID bulma işlemi yapılacak
            # Basit örnek için direkt ID kullanıyoruz
            user_id = int(user) if user.isdigit() else None
        else:
            user_id = int(user)
        
        if not user_id:
            await message.reply("❌ Geçersiz kullanıcı!")
            return
            
        new_balance = BalanceManager.update_balance(user_id, amount)
        await message.reply(f"✅ {user_id} kullanıcısına {amount} puan eklendi.\nYeni bakiye: {new_balance}")
    except Exception as e:
        await message.reply(f"❌ Hata: {str(e)}")

# Diğer fonksiyonlar aynı şekilde kalacak...
