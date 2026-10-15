import logging
import sys
from logging.handlers import RotatingFileHandler

fmt = logging.Formatter("%(asctime)s %(levelname)-7s %(name)s: %(message)s",
                        datefmt="%H:%M:%S")

screen = logging.StreamHandler(sys.stdout)       # 출구 1 — 화면
screen.setLevel(logging.INFO)
screen.setFormatter(fmt)

file = RotatingFileHandler("bot.log", maxBytes=1_000_000,
                           backupCount=3, encoding="utf-8")
file.setLevel(logging.DEBUG)                     # 출구 2 — 파일
file.setFormatter(fmt)

logger = logging.getLogger("deliverybot")
logger.setLevel(logging.DEBUG)                   # 정문은 가장 낮게
logger.addHandler(screen)
logger.addHandler(file)

logger.debug("송장 123 조회 요청")
logger.info("배송 상태: 배송 중")
print("--- bot.log ---")
print(open("bot.log", encoding="utf-8").read().strip())
