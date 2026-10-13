import threading
import time
from work import crunch

N = 15_000_000
start = time.perf_counter()
threads = []
for _ in range(3):
    t = threading.Thread(target=crunch, args=(N,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
print(f"스레드 셋 {time.perf_counter() - start:.1f}초")
