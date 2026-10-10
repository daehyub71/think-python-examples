# 생각하는 파이썬 Part 5 · 람다와 정렬 기준


half = lambda w: w / 2              # lambda 받을 것: 돌려줄 식
print(half(9))                      # 4.5

items = [
    {"name": "노트", "price": 2500, "stock": 40},
    {"name": "펜", "price": 1200, "stock": 120},
    {"name": "가방", "price": 38000, "stock": 7},
    {"name": "자", "price": 1200, "stock": 65},
]

by_price = sorted(items, key=lambda i: i["price"])
print([i["name"] for i in by_price])            # ['펜', '자', '노트', '가방']

by_two = sorted(items, key=lambda i: (i["price"], i["stock"]))
print([i["name"] for i in by_two])              # ['자', '펜', '노트', '가방'] — 가격이 같으면 재고 적은 순
