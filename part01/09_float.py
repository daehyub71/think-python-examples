# 생각하는 파이썬 Part 1 · 실수
# (강의 슬라이드: 실수는 근삿값 · 두 가지 습관)


print(12000 * 1.1)          # 13200.000000000002
print(0.1 + 0.2)            # 0.30000000000000004
print(0.1 + 0.2 == 0.3)     # False

# 습관 ① 실수끼리는 == 대신 "충분히 가까운가"를 묻는다
import math
print(math.isclose(0.1 + 0.2, 0.3))         # True

# 습관 ② 돈 계산에는 Decimal — 숫자는 반드시 따옴표로 감싸서
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))      # 0.3
