# 생각하는 파이썬 Part 6 · 객체 없이 — 데이터와 함수가 따로 놀 때


card = {"name": "한지우", "stamps": 3}

def add(c, count):
    c["stamps"] += count

add(card, 4)
print(card)                         # {'name': '한지우', 'stamps': 7}

card["stamps"] = -5                 # 아무나, 아무 값이나 — 막을 방법이 없다
print(card)                         # {'name': '한지우', 'stamps': -5}
