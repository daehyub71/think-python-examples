# 생각하는 파이썬 Part 4 · get 과 items
# (강의 슬라이드: get() — 없으면 이걸로 · 전부 돌기)

stock = {"A-101": 45, "A-103": 100}

print(stock.get("A-101"))       # 45
print(stock.get("Z-999"))       # None — 없는 키도 오류가 나지 않는다
print(stock.get("Z-999", 0))    # 0    — 없을 때 쓸 값을 정해 둔다
print("A-103" in stock)         # True — in 은 키가 있는지를 묻는다

for code, qty in stock.items(): # 바퀴마다 (키, 값) 한 쌍
    print(f"{code}: {qty}개")
