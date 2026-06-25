# config.py
import socket
import os 

# ============= কনফিগারেশন =============
BOT_TOKEN = os.environ.get("BOT_TOKEN") 
CLIENT_ID = "1517033621469401299"
CLIENT_SECRET = "crnzdgvwhdoWMsXJYS9A_KmKZHHB2a4u"

# ⭐ এগুলো যোগ করুন:
FLASK_PORT = 5000
GUILD_ID = "1515992131725033493"  # আপনার সার্ভার আইডি
VERIFIED_ROLE_ID = "1517035321454366740"  # আপনার রোল আইডি

# লোকাল IP খুঁজে বের করা
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

LOCAL_IP = get_local_ip()
REDIRECT_URI = f"https://invite-tracker-production-7071.up.railway.app/oauth2/callback"

print(f"🌐 আপনার লোকাল IP: {LOCAL_IP}")
print(f"🔗 Redirect URI: {REDIRECT_URI}")
print(f"🆔 Client ID: {CLIENT_ID}")
print(f"📌 Guild ID: {GUILD_ID}")
print(f"📌 Verified Role ID: {VERIFIED_ROLE_ID}")
