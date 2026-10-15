import logging

logging.basicConfig(level=logging.DEBUG,                 # 문턱을 가장 낮게
                    format="%(levelname)-8s %(message)s")

logging.debug("송장 번호 확인 중")
logging.info("배송 조회 시작")
logging.warning("응답이 느립니다 — 다시 시도")
