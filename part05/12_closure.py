# 생각하는 파이썬 Part 5 · 함수를 돌려주는 함수 · 클로저


def make_discount(rate):
    def apply(price):
        return round(price * (1 - rate))    # 바깥의 rate 를 기억한다
    return apply                            # 괄호 없이 — 함수를 돌려준다

staff = make_discount(0.3)
member = make_discount(0.1)
print(staff(50000), member(50000))          # 35000 45000
print(staff.__closure__[0].cell_contents)   # 0.3 — 들고 나온 가방 속

def make_counter():
    count = 0
    def hit():
        nonlocal count                      # 바깥 함수의 이름표를 고쳐 쓰겠다
        count += 1
        return count
    return hit

a = make_counter()
print(a(), a(), a())                        # 1 2 3
b = make_counter()
print(b())                                  # 1 — 가방은 저마다 따로
