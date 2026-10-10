# 생각하는 파이썬 Part 1 · 연산
# (강의 슬라이드: 3부 · 연산자와 표현식)


# 표현식(값이 된다)과 문장(시킬 뿐, 값이 되지 않는다)
print(3 + 4)                # 7 — 표현식
price = 12000               # 문장 — 아무것도 출력하지 않는다

# 나눗셈은 세 가지
print(7 / 2)                # 3.5   나눗셈 — 항상 실수
print(7 // 2)               # 3     몫
print(7 % 2)                # 1     나머지
print(2 ** 10)              # 1024  거듭제곱
print(10 / 2)               # 5.0   딱 떨어져도 실수

# 사탕 17개를 5명에게
print(17 // 5, "개씩,", 17 % 5, "개 남음")

# 계산 순서 — 헷갈리면 괄호
print(2 + 3 * 4)            # 14
print((2 + 3) * 4)          # 20

# 판단하는 연산 — 결과는 True 아니면 False
spent = 870000
budget = 900000
print(spent > budget)       # False — 예산을 넘지 않았다

stock = 5
discontinued = False
print(stock > 0 and not discontinued)   # True — 재고가 있고, 단종이 아니면 판매 가능
