import os
from dotenv import load_dotenv

load_dotenv()
for key in ["BOT_NAME", "CHECK_EVERY", "SEND_MAIL"]:
    value = os.getenv(key)
    print(key, repr(value), type(value).__name__)

send = os.getenv("SEND_MAIL")
print(bool(send))                 # 그대로 bool 로
print(send.lower() == "true")     # 글자로 묻기
