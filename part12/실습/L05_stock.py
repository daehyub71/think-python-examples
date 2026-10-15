import time
from functools import lru_cache

@lru_cache(maxsize=None)
def stock(item):
    time.sleep(0.2)          # 창고에 물어보는 데 0.2초 걸린다고 치자
    return len(item) * 10

start = time.perf_counter()
for item in ["볼펜", "공책", "볼펜", "볼펜", "공책"]:
    stock(item)
print(f"{time.perf_counter() - start:.1f}초")
print(stock.cache_info())
