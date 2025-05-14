import json
import os
from datetime import datetime, timedelta

# Bakiyeleri saklamak için basit JSON dosyası
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
        return data.get(str(user_id), {"balance": 0, "last_daily": None, "ads_today": 0, "last_ad_date": None})

    @staticmethod
    def update_balance(user_id, update_data):
        data = BalanceManager._load_data()
        user_data = data.get(str(user_id), {"balance": 0, "last_daily": None, "ads_today": 0, "last_ad_date": None})
        user_data.update(update_data)
        data[str(user_id)] = user_data
        BalanceManager._save_data(data)

    @staticmethod
    def can_claim_daily(user_id):
        user = BalanceManager.get_balance(user_id)
        if not user["last_daily"]:
            return True
        
        last_claim = datetime.strptime(user["last_daily"], "%Y-%m-%d %H:%M:%S")
        return datetime.now() - last_claim > timedelta(hours=24)

    @staticmethod
    def can_post_ad(user_id):
        user = BalanceManager.get_balance(user_id)
        today = datetime.now().date()
        
        if not user["last_ad_date"]:
            return True
            
        last_ad_date = datetime.strptime(user["last_ad_date"], "%Y-%m-%d %H:%M:%S").date()
        if last_ad_date != today:
            BalanceManager.update_balance(user_id, {"ads_today": 0, "last_ad_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            return True
        
        return user["ads_today"] < 3  # Günlük maks 3 reklam
