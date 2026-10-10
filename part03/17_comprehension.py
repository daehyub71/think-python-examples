# 생각하는 파이썬 Part 3 · 컴프리헨션
# (강의 슬라이드: 4부 · 컴프리헨션)

scores = [88, 45, 92, 30, 71]

# 네 줄
passed = []
for s in scores:
    if s >= 60:
        passed.append(s)
print(passed)               # [88, 92, 71]

# 한 줄 — [무엇을 담을지  for 어디서 꺼낼지  if 어떤 것만]
passed = [s for s in scores if s >= 60]
print(passed)               # [88, 92, 71]

# 바꿔서 담기 — 가격마다 부가세 10%
prices = [1000, 2500, 4000, 7800]
with_tax = [p * 11 // 10 for p in prices]
print(with_tax)             # [1100, 2750, 4400, 8580]
print(prices)               # 원본은 그대로

# 한 줄로 읽힐 때만 씁니다
raw = ["3", "7", "12"]
nums = [int(x) for x in raw]
big = [p for p in prices if p > 3000]
print(nums, big)
