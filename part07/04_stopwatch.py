# 생각하는 파이썬 Part 7 · 실행 시간을 재는 데코레이터


import time

def stopwatch(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()              # 시간을 잴 때 쓰는 정밀한 시계
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__}: {elapsed:.3f}초")
        return result
    return wrapper

@stopwatch
def sum_squares(n):                              # 본문은 제곱의 합만 구한다
    return sum(i * i for i in range(n))

print(sum_squares(3_000_000))
# sum_squares: 0.1xx초   ← 컴퓨터마다 다릅니다
# 8999995500000500000
