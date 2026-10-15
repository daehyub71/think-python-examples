import os
from dotenv import load_dotenv

loaded = load_dotenv()          # .env 를 읽어 환경 변수로 올린다
print("읽었나?", loaded)

name = os.getenv("BOT_NAME", "알리미")
every = int(os.getenv("CHECK_EVERY", "30"))
send_mail = os.getenv("SEND_MAIL", "false").lower() == "true"
print(name, every, send_mail)
