##-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
# powered by DeepSeek Chat ❤️🔥

import os
import json
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import *
import logging

# Logging setup
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
        return cls._balances.setdefault(str(user_id), {
            "balance": 0,
            "last_daily": None,
            "ads_today": 0
        })

BalanceManager.load_balances()

app = Client(
    "reklam_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ==================== MESSAGES ====================
START_MSG = f"""
✨ **Merhaba! Ben {BOT_NAME}** ✨

💎 **Özelliklerim:**
• Günlük {DAILY_BONUS}{CURRENCY} ücretsiz bakiye
• Reklam başına {AD_COST}{CURRENCY}
• Günde max {MAX_ADS_PER_DAY} reklam

📌 Komutlar için /help yazın
"""

HELP_MSG = f"""
📚 **YARDIM MENÜSÜ** 📚

/reklam [metin] - Reklam ver ({AD_COST}{CURRENCY})
/gunluk - Günlük {DAILY_BONUS}{CURRENCY} al
/bakiyem - Bakiyeni kontrol et

👑 **Admin Komutları:**
/addbalance @kullanıcı miktar
/broadcast mesaj

🔗 Reklam Kanalı: @{UPDATE_CHNL}
"""

# ==================== COMMANDS ====================
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_photo(
        photo=START_IMG,
        caption=START_MSG,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🚀 REKLAM VER", callback_data="reklam")],
            [InlineKeyboardButton("💎 BAKİYEM", callback_data="bakiyem")]
        ])
    )

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
        return await message.reply("Örnek: /reklam Ürünümüz çok kaliteli...")

    # Reklamı gönder
    try:
        await client.send_message(
            chat_id=UPDATE_CHNL,
            text=f"📢 **REKLAM**\n\n{message.text.split(maxsplit=1)[1]}\n\n👤 @{message.from_user.username}"
        )
        # Bakiyeyi güncelle
        user_data["balance"] -= AD_COST
        user_data["ads_today"] += 1
        BalanceManager.save_balances()
        
        await message.reply(f"""
✅ Reklam gönderildi!
📌 Kanal: @{UPDATE_CHNL}
💰 Harcanan: {AD_COST}{CURRENCY}
""")
    except Exception as e:
        await message.reply(f"❌ Hata: {str(e)}")

@app.on_message(filters.command("addbalance") & filters.user(SUDO))
async def add_balance(client, message):
    try:
        if len(message.command) < 3:
            return await message.reply("Kullanım: /addbalance @kullanıcı miktar")
        
        # Kullanıcıyı bul
        user = await client.get_users(message.command[1])
        amount = int(message.command[2])
        
        # Bakiye güncelle
        user_data = BalanceManager.get_balance(user.id)
        user_data["balance"] += amount
        BalanceManager.save_balances()
        
        await message.reply(f"""
✅ Bakiye yüklendi!
👤 Kullanıcı: @{user.username}
💰 Miktar: {amount}{CURRENCY}
💳 Yeni bakiye: {user_data['balance']}{CURRENCY}
""")
    except Exception as e:
        await message.reply(f"❌ Hata: {str(e)}")

if __name__ == "__main__":
    logger.info("Bot başlatılıyor...")
    app.run()
    logger.info("Bot durduruldu")
