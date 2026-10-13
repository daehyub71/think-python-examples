import threading
import time

def fetch(name):
    time.sleep(1)
    print(f"{name} 받음")

start = time.perf_counter()
threads = []
for name in ["사진1", "사진2", "사진3"]:
    t = threading.Thread(target=fetch, args=(name,))
    t.start()                    # 일을 시작시킨다
    threads.append(t)
for t in threads:
    t.join()                     # 끝날 때까지 기다린다
print(f"{time.perf_counter() - start:.1f}초")
