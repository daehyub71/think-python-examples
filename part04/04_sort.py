# 생각하는 파이썬 Part 4 · 정렬
# (강의 슬라이드: 정렬)

prices = [3200, 1500, 2700]

print(sorted(prices))       # [1500, 2700, 3200] — 새 리스트를 돌려준다
print(prices)               # [3200, 1500, 2700] — 원본은 그대로

result = prices.sort()      # 원본을 바꾸고, 돌려주는 것은 없다
print(prices)               # [1500, 2700, 3200]
print(result)               # None ← 결과를 변수에 받으면 안 된다
