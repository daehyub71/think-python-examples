# 생각하는 파이썬 Part 1 · 변수
# (강의 슬라이드: 변수 — 값에 붙이는 이름표)


# 값에 이름표 붙이기
stock = 1200
price = 3500
print(stock * price)        # 4200000 — "재고 수량 곱하기 단가"로 읽힌다

# = 은 "같다"가 아니라 "오른쪽 값을 왼쪽 이름표에 붙여라"
count = 10
count = count + 1           # 오른쪽 먼저: 10 + 1 → 11, 그 11에 count 를 새로 붙인다
print(count)                # 11

# == 는 "같은 값인가?"라는 질문 — 답은 True / False
print(stock == 1200)        # True
print(stock == 0)           # False

# 타입은 변수가 아니라 값에 있다 (동적 타이핑)
data = 1200
print(type(data))           # <class 'int'>
data = "무선 마우스"
print(type(data))           # <class 'str'>

# b = a 는 복사가 아니라, 같은 값에 이름표를 하나 더 붙이는 것
a = 1200
b = a
print(id(a) == id(b))       # True
