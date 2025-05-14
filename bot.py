#
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
        return data.get(str(user_id), {"balance": 0, "last_daily": None})

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

async def send_startup_message():
    try:
        await Mukesh.send_message(
            chat_id=UPDATE_CHNL,
            text=f"✅ **{BOT_NAME} başarıyla başlatıldı!**\n\n"
                 f"▸ Versiyon: v2.1\n"
                 f"▸ Sahip: @{OWNER_USERNAME}\n"
                 f"▸ Zaman: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
            disable_web_page_preview=True
        )
    except Exception as e:
        logging.error(f"Kanal bildirimi gönderilemedi: {e}")

StartTime = time.time()
Mukesh = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START = f"""
๏ 𝗠𝗲𝗿𝗵𝗮𝗯𝗮 🌹

Reklam Botu ile kolayca reklam verebilirsiniz!
Günlük ücretsiz bakiye kazanın.
"""

# ... (mevcut kodlarınız aynen kalıyor) ...

if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        Mukesh.start()
        # Bot başladığında kanala mesaj gönder
        asyncio.get_event_loop().run_until_complete(send_startup_message())
        
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
