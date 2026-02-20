import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
BASE_DIR = Path(__file__).parent.parent
load_dotenv(BASE_DIR / '.env')  # Root .env
load_dotenv(Path(__file__).parent / '.env')  # Local bot/.env

# Bot token
BOT_TOKEN = os.getenv('BOT_TOKEN', '').strip()

# Helper to get and sanitize URLs
def get_sanitized_env(key, default):
    val = os.getenv(key, default).strip()
    if not val or 'your-new' in val or 'example.com' in val:
        return default.strip()
    return val

# Backend API URL
BACKEND_API_URL = get_sanitized_env('BACKEND_API_URL', 'https://humo-tezkor-backend.onrender.com/api').rstrip('/')

# Web App URLs
WEB_APP_SHOP_URL = get_sanitized_env('WEB_APP_SHOP_URL', 'https://humo-tezkor-frontend.vercel.app').rstrip('/')
WEB_APP_CHAT_URL = get_sanitized_env('WEB_APP_CHAT_URL', 'https://humo-tezkor-frontend.vercel.app/chat').rstrip('/')
WEB_APP_ORDERS_URL = get_sanitized_env('WEB_APP_ORDERS_URL', 'https://humo-tezkor-frontend.vercel.app/orders').rstrip('/')
