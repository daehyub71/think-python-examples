import sys
import tracemalloc

tracemalloc.start()
names = [f"회원{i:05d}" for i in range(100_000)]
current = tracemalloc.get_traced_memory()[0]
tracemalloc.stop()

print(f"getsizeof   {sys.getsizeof(names) / 1024:,.0f}KB")
print(f"tracemalloc {current / 1024:,.0f}KB")
