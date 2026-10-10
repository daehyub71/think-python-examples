# 생각하는 파이썬 Part 5 · 표준 라이브러리 맛보기


import datetime
import math
import random
from pathlib import Path

print(math.ceil(7.2), math.pi)                          # 8 3.141592653589793

random.seed(7)                                          # 출발점을 고정 — 같은 결과가 다시 나온다
print(random.randint(1, 6))                             # 3
print(random.choice(["김밥", "라면", "돈가스"]))         # 김밥

print(datetime.date(2026, 10, 8) + datetime.timedelta(days=100))    # 2027-01-16
print(Path("report.csv").suffix)                        # .csv
