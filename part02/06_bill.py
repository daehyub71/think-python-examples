# 생각하는 파이썬 Part 2 · 함수와 이름표
# (강의 슬라이드: 함수를 부르면 작업대가 하나 쌓인다)


def bill(price, qty):
    amount = price * qty        # price, qty, amount — 함수가 도는 동안만 있는 이름표
    return amount

result = bill(4500, 4)
print(result)                   # 18000 — result 가 가리키고 있어 살아남은 값

# 함수가 끝나면 작업대와 이름표는 사라집니다.
# 아래 줄의 주석을 풀면 NameError 가 납니다 — 함수 안의 이름표는 밖에서 쓸 수 없습니다.
# print(amount)
