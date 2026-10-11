# 생각하는 파이썬 Part 7 · 데코레이터의 뼈대 — 어떤 함수든 감쌀 수 있게


def log_call(func):                      # ① 감쌀 함수를 받는다
    def wrapper(*args, **kwargs):        # ② 무엇이 오든 통째로 받는다
        print(f"{func.__name__} 호출")
        result = func(*args, **kwargs)   # ③ 받은 그대로 원래 함수에 넘긴다
        return result                    # ④ 결과를 그대로 돌려준다
    return wrapper                       # ⑤ 괄호 없이 — 함수 그 자체를 돌려준다

@log_call
def total(prices):
    return sum(prices)

@log_call
def discount(price, rate=0.1):
    return round(price * (1 - rate))

print(total([3000, 4500, 2500]))         # total 호출 / 10000
print(discount(20000, rate=0.25))        # discount 호출 / 15000
