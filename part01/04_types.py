# 생각하는 파이썬 Part 1 · 타입
# (강의 슬라이드: 값에는 종류가 있다 · type())


stock = 1200                # int   — 셀 수 있는 개수
price = 3500.0              # float — 잴 수 있는 양
name = "무선 마우스"         # str   — 적는 말
sold_out = False            # bool  — 예/아니오

print(type(stock), type(price), type(name), type(sold_out))

print(type(7))              # <class 'int'>
print(type(7.0))            # <class 'float'>  소수점이 붙으면 타입이 달라진다
print(type(True))           # <class 'bool'>

# 따옴표로 감싸면 숫자가 아니라 글자입니다.
print(type("1200"))         # <class 'str'>
print("100" + "200")        # 100200  ← 더한 것이 아니라 이어 붙인 것
