##-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
# powered by DeepSeek Chat ❤️🔥

import os
import json
from datetime import datetime
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import *
import asyncio
import logging

# Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BalanceManager:
    _balances = {}

    @classmethod
    def load_balances(cls):
        try:
            if os.path.exists("balances.json"):
                with open("balances.json", "r") as f:
                    cls._balances = json.load(f)
        except Exception as e:
            logger.error(f"Balance load error: {e}")

    @classmethod
    def save_balances(cls):
        try:
            with open("balances.json", "w") as f:
                json.dump(cls._balances, f, indent=4)
        except Exception as e:
            logger.error(f"Balance save error: {e}")

    @classmethod
    def get_balance(cls, user_id):
        return cls._balances.get(str(user_id), {"balance": 0, "last_daily": None, "ads_today": 0})

    @classmethod
    def update_balance(cls, user_id, amount):
        user_data = cls._balances.setdefault(str(user_id), {"balance": 0, "last_daily": None, "ads_today": 0})
        user_data["balance"] = max(0, user_data["balance"] + amount)
        cls.save_balances()
        return user_data["balance"]

# Initialize Balance Manager
BalanceManager.load_balances()

app = Client(
    "reklam_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

# ==================== START MESSAGE ====================
START_MESSAGE = f"""
✨ **Merhaba! Ben {BOT_NAME}** ✨

🚀 Reklam botu olarak hizmetinizdeyim!

💎 **Özelliklerim:**
• Günlük {DAILY_BONUS}₺ ücretsiz bakiye
• Kolay reklam yönetimi
• Admin kontrol paneli

📌 Komutlar için /help yazın
"""

START_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("💎 BAKİYEM", callback_data="my_balance"),
     InlineKeyboardButton("🚀 REKLAM VER", callback_data="post_ad")],
    [InlineKeyboardButton("📚 YARDIM", callback_data="help_menu"),
     InlineKeyboardButton("👑 SAHİP", url=f"t.me/{OWNER_USERNAME}")]
])

# ==================== HELP MESSAGE ====================
HELP_MESSAGE = f"""
📚 **YARDIM MENÜSÜ** 📚

🔹 **Temel Komutlar:**
/start - Botu başlat
/help - Yardım menüsü
/bakiyem - Bakiye kontrol

💰 **Bakiye Sistemi:**
/gunluk - Günlük {DAILY_BONUS}₺ al
/reklam - Reklam ver ({AD_COST}₺)

👑 **Admin Komutları:**
/addbalance [@kullanıcı] [miktar] - Bakiye ekle
/broadcast [mesaj] - Toplu duyuru

📢 Reklamlarınız: @{UPDATE_CHNL}
"""

HELP_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔙 ANA MENÜ", callback_data="main_menu")]
])

# ==================== COMMAND HANDLERS ====================
@app.on_message(filters.command("start"))
async def start_command(client, message):
    try:
        await message.reply_photo(
            photo=START_IMG,
            caption=START_MESSAGE,
            reply_markup=START_BUTTONS
        )
    except Exception as e:
        logger.error(f"Start error: {e}")

@app.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_text(
        HELP_MESSAGE,
        reply_markup=HELP_BUTTONS
    )

@app.on_message(filters.command("bakiyem"))
async def balance_command(client, message):
    balance = BalanceManager.get_balance(message.from_user.id)["balance"]
    await message.reply(f"💰 Bakiyeniz: {balance}₺")

@app.on_message(filters.command("reklam"))
async def reklam_ver(client, message):
    user_data = BalanceManager.get_balance(message.from_user.id)
    
    # Bakiye kontrol
    if user_data["balance"] < AD_COST:
        return await message.reply(f"""
❌ Yetersiz bakiye!
Gerekli: {AD_COST}{CURRENCY}
Bakiyeniz: {user_data['balance']}{CURRENCY}
""")

    # Reklam metni kontrol
    if len(message.text.split()) < 2:
        return await message.reply("✅ KULLANIM :\n\n /reklam [ BENİMLE EVLENİRMİSİN 🔮 ]")

    # Reklamı gönder
    try:
        await client.send_message(
            chat_id=UPDATE_CHNL,
            text=f"📢 **REKLAM**\n\n{message.text.split(maxsplit=1)[1]}\n\n👤 @{message.from_user.username}"
        )
        # Bakiyeyi güncelle
        BalanceManager.update_balance(message.from_user.id, -AD_COST)
        
        await message.reply(f"""
✅ Reklam gönderildi!
📌 Kanal: @{UPDATE_CHNL}
💰 Harcanan: {AD_COST}{CURRENCY}
""")
    except Exception as e:
        await message.reply(f"❌ Hata: {str(e)}")

# ==================== CALLBACK HANDLERS ====================
@app.on_callback_query(filters.regex("^main_menu$"))
async def main_menu_callback(client, query):
    await query.message.edit_text(
        START_MESSAGE,
        reply_markup=START_BUTTONS
    )

@app.on_callback_query(filters.regex("^help_menu$"))
async def help_menu_callback(client, query):
    await query.message.edit_text(
        HELP_MESSAGE,
        reply_markup=HELP_BUTTONS
    )

@app.on_callback_query(filters.regex("^my_balance$"))
async def balance_callback(client, query):
    balance = BalanceManager.get_balance(query.from_user.id)["balance"]
    await query.message.edit_text(
        f"💰 **Bakiyeniz:** {balance}₺",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Geri", callback_data="main_menu")]
        ])
    )

# ==================== ADMIN COMMANDS ====================
@app.on_message(filters.command("addbalance") & filters.user(SUDO))
async def add_balance_command(client, message):
    try:
        if len(message.command) < 3:
            return await message.reply("Kullanım: /addbalance @kullanıcı miktar")

        username = message.command[1].lstrip("@")
        amount = int(message.command[2])

        try:
            user = await client.get_users(username)
            new_balance = BalanceManager.update_balance(user.id, amount)
            await message.reply(f"""
✅ Bakiye Yüklendi!
👤 Kullanıcı: @{user.username}
💰 Miktar: {amount}₺
💳 Yeni Bakiye: {new_balance}₺
""")
        except Exception as e:
            await message.reply(f"❌ Kullanıcı bulunamadı: {e}")
    except Exception as e:
        await message.reply(f"❌ Hata: {e}")

# ==================== MAIN ====================
if __name__ == "__main__":
    logger.info("Starting bot...")
    app.run()
    logger.info("Bot stopped")
