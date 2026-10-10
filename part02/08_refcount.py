# 생각하는 파이썬 Part 2 · 참조 카운트
# (강의 슬라이드: 이름표를 세어 본다)


import sys

shelf = [15, 25, 35]
print(sys.getrefcount(shelf))   # 2 — 세어 달라고 건네는 순간 한 장이 잠깐 더 붙는다

same = shelf                    # 복사가 아니라 이름표 한 장 더
print(sys.getrefcount(shelf))   # 3

del same                        # 이름표 한 장 떼기
print(sys.getrefcount(shelf))   # 2

# 숫자 자체보다 늘고 주는 방향을 보세요.
