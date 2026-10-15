import tracemalloc

tracemalloc.start()
prices = list(range(500_000))
taxed = [p * 11 // 10 for p in prices]   # 잠깐 둘이 함께 있다
del prices
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"지금 {current / 1024 / 1024:.1f}MB")
print(f"최고 {peak / 1024 / 1024:.1f}MB")
