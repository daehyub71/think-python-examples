# 생각하는 파이썬 Part 4 · 리스트와 인덱스
# (강의 슬라이드: 리스트 — 값을 줄 세워 담는다)

sales = [120, 340, 90, 510, 280]    # 닷새 치 매출(만 원)

print(sales[0])             # 120 — 번호(인덱스)는 0부터
print(sales[2])             # 90
print(sales[-1])            # 280 — -1 은 맨 뒤
print(len(sales))           # 5 — 값은 5개, 마지막 번호는 4

# print(sales[5])           # 주석을 풀면 IndexError: list index out of range
