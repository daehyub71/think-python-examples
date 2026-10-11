# 생각하는 파이썬 Part 7 · 함수를 받아 함수를 돌려준다 — 손으로 감싸기


def log_call(func):                  # 함수를 받아서
    def wrapper(prices):
        print(f"{func.__name__} 호출")   # 앞에 할 일을 끼우고
        return func(prices)              # 원래 함수를 부른 뒤, 결과를 그대로 돌려준다
    return wrapper                   # 새 함수를 돌려준다

def total(prices):
    return sum(prices)

total = log_call(total)              # 감싼 새 함수로 바꿔 붙인다 — total 의 코드는 그대로
print(total([3000, 4500, 2500]))
# total 호출
# 10000
