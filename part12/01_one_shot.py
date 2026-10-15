import time

for _ in range(5):
    start = time.perf_counter()
    total = sum(range(100))
    took = time.perf_counter() - start
    print(f"{took * 1e6:.2f}µs")
