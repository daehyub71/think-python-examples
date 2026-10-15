import logging
import sys

logger = logging.getLogger("deliverybot")
logger.setLevel(logging.DEBUG)          # 정문

screen = logging.StreamHandler(sys.stdout)
screen.setLevel(logging.DEBUG)          # 출구
logger.addHandler(screen)

logger.debug("보일까? — debug")
logger.info("보일까? — info")
