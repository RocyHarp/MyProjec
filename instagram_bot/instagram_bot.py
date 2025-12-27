import os
import requests
from dotenv import load_dotenv
from google import genai
from instagrapi import Client
from PIL import Image

# Завантажуємо змінні з файлу .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SESSION_ID = os.getenv("INSTA_SESSION_ID")
MY_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.1 Safari/605.1.15"

def run_bot():
    print("\n🚀 ЗАПУСК БОТА...")
    
    if not GEMINI_API_KEY or not SESSION_ID:
        print("❌ Помилка: Не знайдено API KEY або SESSION ID у файлі .env")
        return

    cl = Client()
    cl.set_user_agent(MY_USER_AGENT)
    session_file = "insta_session.json"

    try:
        if os.path.exists(session_file):
            cl.load_settings(session_file)
            print("✅ Сесію завантажено з файлу")
        else:
            cl.login_by_sessionid(SESSION_ID)
            cl.dump_settings(session_file)
            print("💾 Нову сесію збережено")
        
        user_info = cl.account_info()
        print(f"✅ Успіх: Авторизовано як @{user_info.username}")
    except Exception as e:
        print(f"❌ Помилка входу: {e}")
        # Якщо сесія невалідна, видаляємо файл
        if os.path.exists(session_file): 
            os.remove(session_file)
        return

    print("🤖 Gemini пише підпис...")
    caption = "Beautiful moments. ✨ #lifestyle #vibes" # Дефолтний підпис
    try:
        client_ai = genai.Client(api_key=GEMINI_API_KEY)
        ai_response = client_ai.models.generate_content(
            model="gemini-1.5-flash", 
            contents="Short aesthetic Instagram caption about a perfect day. English. 3 hashtags. No quotes."
        )
        if ai_response.text:
            caption = ai_response.text.strip()
            print(f"📝 Згенеровано: {caption}")
    except Exception as e:
        print(f"⚠️ Помилка Gemini (використовую дефолтний підпис): {e}")

    print("📸 Качаємо фото...")
    img_filename = "post_ready.jpg"
    try:
        response = requests.get("https://picsum.photos/1080/1080", stream=True, allow_redirects=True)
        response.raise_for_status()
        
        with Image.open(response.raw) as img:
            img.convert("RGB").save(img_filename, "JPEG")
    except Exception as e:
        print(f"❌ Помилка завантаження фото: {e}")
        return

    print("📤 Публікуємо...")
    try:
        media = cl.photo_upload(img_filename, caption=caption)
        print(f"🎉 Готово! Пост опубліковано. ID: {media.pk}")
    except Exception as e:
        print(f"❌ Помилка публікації: {e}")
    finally:
        if os.path.exists(img_filename):
            os.remove(img_filename)

if __name__ == "__main__":
    run_bot()