import os

# Telegram API Bilgileri
API_ID = int(os.environ.get("API_ID", "20658336"))
API_HASH = os.environ.get("API_HASH", "cedfb5fb4ffee7ecc746b28afc7925e3") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "{BOT_TOKEN}")

# Bot Bilgileri
BOT_USERNAME = os.environ.get("BOT_USERNAME", "LunaGramBot") 
BOT_NAME = os.environ.get("BOT_NAME", "ᴛʜᴇɴᴀ ᴀɪ")
START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/4746e2442a584f37dcc86.jpg")
STKR = os.environ.get("STKR", "CAACAgEAAx0CRjAUHgABAsULZASkFZUsTQTw2k-FvC2SBJnd-vAAAokCAALW9iBFzemsQBDIqWkuBA")

# Yönetici ve Kısıtlamalar
SUDO = list(map(int, os.environ.get("SUDO", "5910057231").split()))
BANNED_USERS = os.environ.get("BANNED_USERS", None)

# Kanal ve Grup Bilgileri
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "ReklamAdssdemo")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "MuratVio")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "Bot4Chan")

# Bakiye ve Reklam Sistemi
DAILY_BONUS = 20  # Günlük bakiye bonusu
AD_COST = 30  # Reklam verme maliyeti
MAX_ADS_PER_DAY = 3  # Kullanıcı başına günlük maks reklam

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

# Ödeme Bilgileri
PAYMENT_INFO = """
💳 Ödeme Yöntemleri:
- Banka Havalesi: TRXX XXXX XXXX XXXX
- Kripto: USDT (TRC20)
"""

# Reklam Kuralları
AD_RULES = f"""
📢 REKLAM KURALLARI:

1. Günlük {DAILY_BONUS} ücretsiz bakiye
2. Reklam başına {AD_COST} bakiye gerekiyor
3. Günde max {MAX_ADS_PER_DAY} reklam
4. Ödeme sonrası iade yoktur
"""
