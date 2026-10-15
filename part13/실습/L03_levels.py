import logging

logging.basicConfig(level=logging.INFO)

logging.debug("송장 번호 확인 중")
logging.info("배송 조회 시작")
logging.warning("응답이 느립니다")
logging.error("조회 실패")
logging.critical("서버 연결 끊김")
