import logging

logging.basicConfig(format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger("deliverybot")

try:
    qty = int("세 개")
except ValueError:
    logger.exception("수량 읽기 실패")
