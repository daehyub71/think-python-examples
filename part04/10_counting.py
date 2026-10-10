# 생각하는 파이썬 Part 4 · 세기
# (강의 슬라이드: 가장 많이 쓰는 패턴 — 세기)

defects = ["찍힘", "스크래치", "찍힘", "도색", "찍힘", "스크래치", "찍힘"]

counts = {}
for d in defects:
    counts[d] = counts.get(d, 0) + 1    # 지금까지 센 횟수(없으면 0)에 1을 더해 다시 적는다
print(counts)               # {'찍힘': 4, '스크래치': 2, '도색': 1}

from collections import Counter         # 세는 일 전용 도구
print(Counter(defects).most_common(1))  # [('찍힘', 4)]
