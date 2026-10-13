import threading
import time
from team import run_together

visitors = 0
lock = threading.Lock()

def enter(times):
    global visitors
    for _ in range(times):
        with lock:
            now = visitors
            time.sleep(0.001)
            visitors = now + 1

run_together(enter, threads=3, times=100)
print(visitors)
