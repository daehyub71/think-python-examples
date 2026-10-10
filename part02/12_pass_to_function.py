# 생각하는 파이썬 Part 2 · 함수에 값 넘기기
# (강의 슬라이드: 함수에 넘기면 · 원본을 지키려면)


def add_one(n):
    n += 1                      # 숫자는 불변 — 새 값을 만들어 n 만 옮겨 붙인다
    return n

count = 10
print(add_one(count))           # 11
print(count)                    # 10 — 바깥은 그대로

def add_item(items):
    items.append("풀")           # 리스트는 가변 — 가리키던 그 객체를 제자리에서 고친다

cart = ["펜", "자"]
add_item(cart)
print(cart)                     # ['펜', '자', '풀'] — 바깥이 바뀌었다

# 원본을 지키려면 복사본을 넘긴다
cart = ["펜", "자"]
add_item(cart.copy())
print(cart)                     # ['펜', '자'] — 원본은 그대로
