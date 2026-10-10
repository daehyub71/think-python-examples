# 생각하는 파이썬 Part 5 · 함수 — 정의하고 부르기


def box_fee(weight):                # 정의 — 적어 두기만 한다
    return 3000 + weight * 500      # 기본요금 3,000원 + 1kg마다 500원

print(box_fee(4))                   # 5000 — 괄호를 붙여 부를 때 실행된다
print(box_fee(10))                  # 8000
print(box_fee(weight=10))           # 8000 — 이름을 적어 넘겨도 된다
