import time

def stopwatch(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__}: {elapsed:.3f}초")
        return result
    return wrapper

@stopwatch
def sum_squares(n):
    return sum(i * i for i in range(n))

@stopwatch
def count_even(n):
    return len([i for i in range(n) if i % 2 == 0])

sum_squares(3_000_000)
count_even(3_000_000)
