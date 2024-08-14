import requests

from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

def send_message(text):
    BOT_TOKEN = env.str("BOT_TOKEN")
    CHAT_ID = env.str("CHAT_ID")
    PHOTO = "https://cdn.streamelements.com/uploads/cc108537-e0f0-47a2-b330-7b56bcfecd5e.png"
    TEXT = text
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendphoto?chat_id={CHAT_ID}&photo={PHOTO}&caption={TEXT}"
    response = requests.get(url)
    # print(response.status_code)