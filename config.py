import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
BASE_DIR = Path(__file__).parent.parent
load_dotenv(BASE_DIR / '.env')  # Root .env
load_dotenv(Path(__file__).parent / '.env')  # Local bot/.env

# Bot token
BOT_TOKEN = os.getenv('BOT_TOKEN', '')

# Backend API URL
BACKEND_API_URL = os.getenv('BACKEND_API_URL', 'https://punyo-market-backend.onrender.com/api')

# Web App URLs
def get_valid_url(env_key, default_url):
    url = os.getenv(env_key, '')
    if not url or 'your-webapp.com' in url or 'example.com' in url:
        return default_url
    return url

WEB_APP_SHOP_URL = get_valid_url('WEB_APP_SHOP_URL', 'https://frontend-gold-delta-10.vercel.app')
WEB_APP_CHAT_URL = get_valid_url('WEB_APP_CHAT_URL', 'https://frontend-gold-delta-10.vercel.app/chat')
WEB_APP_ORDERS_URL = get_valid_url('WEB_APP_ORDERS_URL', 'https://frontend-gold-delta-10.vercel.app/orders')
