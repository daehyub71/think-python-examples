# 생각하는 파이썬 Part 7 · @ 는 "이름 = 데코레이터(이름)" 을 대신 적어 준다


def log_call(func):
    def wrapper(prices):
        print(f"{func.__name__} 호출")
        return func(prices)
    return wrapper

@log_call                            # total = log_call(total) 과 똑같다
def total(prices):
    return sum(prices)

print(total([3000, 4500, 2500]))
# total 호출
# 10000
