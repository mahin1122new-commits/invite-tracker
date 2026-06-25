# index.py
import threading
import time
from config import BOT_TOKEN, REDIRECT_URI, FLASK_PORT
from bot import bot
from web import run_flask

# ============= মেইন =============
if __name__ == "__main__":
    print("=" * 60)
    print("🤖 Discord বট + Flask সার্ভার চালু হচ্ছে...")
    print("=" * 60)
    print(f"🌐 আপনার লোকাল IP: https://invite-tracker-production-7071.up.railway.app/")
    print(f"🔗 Redirect URI: {REDIRECT_URI}")
    print(f"🔌 Flask Port: {FLASK_PORT}")
    print("=" * 60)
    print("⚠️ Discord Developer Portal এ এই URI যোগ করুন:")
    print(f"   {REDIRECT_URI}")
    print("=" * 60)
    
    # Flask চালান আলাদা থ্রেডে
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    # Flask শুরু হওয়ার জন্য অপেক্ষা
    time.sleep(3)
    
    # বট চালান
    try:
        bot.run(BOT_TOKEN)
    except Exception as e:
        print(f"❌ বট error: {str(e)}")
