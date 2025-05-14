import os

# Telegram API
API_ID = int(os.environ.get("API_ID", "20658336"))
API_HASH = os.environ.get("API_HASH", "cedfb5fb4ffee7ecc746b28afc7925e3") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")  # Burayı güncelleyin

# Yetkililer
SUDO_USERS = list(map(int, os.environ.get("SUDO", "8141229305").split()))
BANNED_USERS = list(map(int, os.environ.get("BANNED_USERS", "").split())) if os.environ.get("BANNED_USERS") else []

# Bot Bilgileri
BOT_USERNAME = os.environ.get("BOT_USERNAME", "LunaGramBot")
BOT_NAME = os.environ.get("BOT_NAME", "ᴛʜᴇɴᴀ ᴀɪ")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "MuratVio")

# Medya
START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/4746e2442a584f37dcc86.jpg")
STKR = os.environ.get("STKR", "CAACAgEAAx0CRjAUHgABAsULZASkFZUsTQTw2k-FvC2SBJnd-vAAAokCAALW9iBFzemsQBDIqWkuBA")

# Kanal/Grup
SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "Bot4Chan")
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "ReklamAdssdemo")
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")

# Bakiye Sistemi
DAILY_BONUS = 20
AD_COST = 30
MAX_ADS_PER_DAY = 3
CURRENCY = "₺"

# Reklam Paketleri
AD_PRICES = {
    "standard": 50,
    "premium": 100, 
    "sponsored": 200
}

AD_DURATIONS = {
    "standard": "24 saat",
    "premium": "3 gün",
    "sponsored": "1 hafta"
}

# Ödeme
PAYMENT_INFO = """
💳 Ödeme Yöntemleri:
- Banka: TRXX XXXX XXXX XXXX
- USDT (TRC20): TAbc...xyz
"""

AD_RULES = f"""
📢 REKLAM KURALLARI:
1. Günlük {DAILY_BONUS}{CURRENCY} ücretsiz bakiye
2. Reklam başına {AD_COST}{CURRENCY}
3. Günde max {MAX_ADS_PER_DAY} reklam
"""
