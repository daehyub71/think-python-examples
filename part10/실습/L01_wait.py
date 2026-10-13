import threading
import time

def fetch(name):
    time.sleep(1)
    print(f"{name} 받음")

start = time.perf_counter()
threads = []
for name in ["사진1", "사진2", "사진3"]:
    t = threading.Thread(target=fetch, args=(name,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
print(f"{time.perf_counter() - start:.1f}초")

# 영상의 마지막 단계에서는 위의 두 줄(for t in threads: t.join())을 지워, 0.0초가 먼저 찍히는 것을 보였습니다.
