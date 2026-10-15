import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

BOT_NAME = os.getenv("BOT_NAME", "알리미")
CHECK_EVERY = int(os.getenv("CHECK_EVERY", "30"))
SEND_MAIL = os.getenv("SEND_MAIL", "false").lower() == "true"
API_TOKEN = os.getenv("API_TOKEN", "")
if not API_TOKEN:                        # 없거나 비어 있으면 바로 멈춘다
    raise SystemExit("API_TOKEN 이 비어 있습니다 — .env 를 확인하세요")
