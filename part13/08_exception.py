import logging

logging.basicConfig(format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger("deliverybot")

def days_left(text):
    return int(text) - 1

try:
    days_left("모레")
except ValueError:
    logger.exception("남은 날짜 계산 실패")     # 오류 위치까지 함께 남긴다
