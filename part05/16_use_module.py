# 생각하는 파이썬 Part 5 · 모듈 가져다 쓰기 (같은 폴더의 fees.py)


import math
import fees                         # 같은 폴더의 fees.py — .py 는 떼고 적는다

print(math.floor(7.8), math.gcd(24, 36))   # 7 12
print(fees.box_fee(4))              # 5000 — fees.py 의 시험 줄은 실행되지 않는다
print(fees.BASE)                    # 3000
print(fees.__name__, __name__)      # fees __main__
