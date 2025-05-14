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
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "ReklamAdssdemo")  # Reklamların gideceği kanal
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "MuratVio")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "Bot4Chan")

# Reklam Ayarları
AD_PRICES = {
    "standard": 50,  # Standart reklam ücreti (örneğin 50 TL)
    "premium": 100,  # Premium reklam ücreti
    "sponsored": 200  # Sponsorlu içerik ücreti
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
- Diğer: Kanaldan iletişime geçin
"""

# Reklam Kuralları
AD_RULES = """
📢 Reklam Kuralları:
1. Yasa dışı içerik yasaktır
2. Spam yapılamaz
3. Reklam onayı 1 saat içinde verilir
4. Ödeme sonrası iade yoktur
"""
