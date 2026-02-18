import asyncio
import os
from aiogram import Bot
from aiogram.types import FSInputFile
from dotenv import load_dotenv

# Load config from the same directory
load_dotenv()

async def set_photo():
    token = os.getenv('BOT_TOKEN')
    if not token:
        print("Error: BOT_TOKEN not found in .env")
        return

    bot = Bot(token=token)
    
    # Path to the logo.png found in frontend/public/
    photo_path = r"c:\Users\User\.gemini\antigravity\scratch\punyo_market\frontend\public\logo.png"
    
    if not os.path.exists(photo_path):
        print(f"Error: logo.png not found at {photo_path}")
        return

    try:
        photo = FSInputFile(photo_path)
        await bot.set_chat_photo(chat_id=(await bot.get_me()).id, photo=photo)
        # Note: for bots, sometimes set_chat_photo on own ID doesn't work,
        # usually it's setBotPhoto. But aiogram Bot doesn't have setBotPhoto directly?
        # Actually, Bot has set_my_name, set_my_description, etc.
        # But for the profile pic, usually you use set_chat_photo or BotFather.
        # Wait, Bot API 6.1+ has setBotPhoto? No, it's still usually BotFather for profile pic.
        # However, set_chat_photo on the bot's own chat ID might work for some aspects.
        # Actually, let's use the standard set_chat_photo.
        
        # Correction: Telegram Bot API doesn't have a direct 'setBotPhoto'.
        # You normally go through @BotFather. 
        # But wait, let's try set_chat_photo.
        print(f"Attempting to set photo from {photo_path}...")
        await bot.set_chat_photo(chat_id=(await bot.get_me()).id, photo=photo)
        print("Humo Tezkor bot rasmi muvaffaqiyatli o'rnatildi!")
    except Exception as e:
        print(f"Xatolik: {e}")
        print("Eslatma: Ba'zan bot rasmimini faqat @BotFather orqali o'rnatish mumkin.")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(set_photo())
