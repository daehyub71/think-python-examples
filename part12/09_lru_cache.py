import time
from functools import lru_cache

def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

@lru_cache(maxsize=None)          # 답을 기억해 둔다
def fib_memo(n):
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)

for f in (fib, fib_memo):
    start = time.perf_counter()
    answer = f(32)
    print(f.__name__, answer, f"{(time.perf_counter() - start) * 1000:.3f}ms")
print(fib_memo.cache_info())
