# 생각하는 파이썬 Part 5 · 고차 함수 · map · filter


def convert(func, values):        # 함수를 받는 함수
    return [func(v) for v in values]

print(convert(len, ["펜", "가방", "노트북"]))       # [1, 2, 3]
print(convert(lambda p: p // 100 * 100, [1250, 990]))   # [1200, 900] — 100원 아래 버리기

prices = [2500, 1200, 38000, 1200]
print(list(map(lambda p: p // 100, prices)))       # [25, 12, 380, 12]
print(list(filter(lambda p: p >= 2000, prices)))   # [2500, 38000]
print([p // 100 for p in prices if p >= 2000])     # [25, 380] — 실무에서는 컴프리헨션이 더 흔하다
