# 생각하는 파이썬 Part 13 · 직접 해보기 풀이 (②~④)
# 실행: python-dotenv 를 깐 가상환경을 켜고  python3 practice_answers.py
# ① 은 터미널 명령이라 아래 주석으로 적었습니다.

# ① 두 도구함에 다른 버전 ----------------------------------------------------
#   $ mkdir 옛프로젝트 새프로젝트
#   $ cd 옛프로젝트 && python3 -m venv .venv && source .venv/bin/activate
#   (.venv) $ pip install "rich==13.9.4"
#   (.venv) $ pip show rich                  → Version: 13.9.4 줄을 본다
#   (.venv) $ deactivate && cd ../새프로젝트
#   $ python3 -m venv .venv && source .venv/bin/activate
#   (.venv) $ pip install rich
#   (.venv) $ pip show rich                  → Version: 15.0.0 (그때의 최신)
#   한 컴퓨터에 두 버전이 따로 산다. 윈도우는 source 대신 .venv\Scripts\activate

import logging
import os
import sys
import tempfile
from logging.handlers import RotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv

# ② 설정 세 개 --------------------------------------------------------------
work = Path(tempfile.mkdtemp())
(work / ".env").write_text("MAX_ITEMS=20\nDRY_RUN=False\n", encoding="utf-8")   # SHOP_URL 은 일부러 비웠다
load_dotenv(work / ".env")

MAX_ITEMS = int(os.getenv("MAX_ITEMS", "10"))
DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"       # "False" → False
SHOP_URL = os.getenv("SHOP_URL", "https://shop.example.com")    # 없으면 기본값
print("②", MAX_ITEMS, DRY_RUN, SHOP_URL)
print("   함정:", bool(os.getenv("DRY_RUN")))                     # True — 글자가 들어 있으니 참

# ③ 토큰 가리기 --------------------------------------------------------------
def mask_tail(secret, keep=4):
    """뒤 keep 글자만 남기고 가린다"""
    if len(secret) <= keep:
        return "*" * len(secret)
    return "*" * (len(secret) - keep) + secret[-keep:]

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s", stream=sys.stdout)
logger = logging.getLogger("deliverybot")
token = "demo-7f3a9c"
logger.info("택배 회사에 접속 — 토큰 %s", mask_tail(token))     # *******3a9c

# ④ 파일이 몇 개 생길까 -----------------------------------------------------
log_path = work / "test.log"
rot = logging.getLogger("rotate-demo")
rot.setLevel(logging.INFO)
rot.propagate = False                      # 화면(위의 basicConfig)으로는 보내지 않는다
handler = RotatingFileHandler(log_path, maxBytes=300, backupCount=2, encoding="utf-8")
handler.setFormatter(logging.Formatter("%(message)s"))
rot.addHandler(handler)
for n in range(1, 101):
    rot.info("송장 %03d 조회", n)
handler.close()
files = sorted(p.name for p in work.glob("test.log*"))
print("④", files)
print("   지금 파일의 첫 줄:", log_path.read_text(encoding="utf-8").splitlines()[0])
# 300바이트를 넘길 때마다 test.log → test.log.1 → test.log.2 로 밀려나고, 그보다 오래된 것은 지워진다.
# 그래서 100줄을 남겨도 파일은 세 개(test.log, test.log.1, test.log.2)뿐이고, 앞쪽 줄들은 사라졌다.
