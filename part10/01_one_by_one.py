import time

def fetch(name):
    time.sleep(1)                # 내려받기를 기다린다
    print(f"{name} 받음")

start = time.perf_counter()
for name in ["사진1", "사진2", "사진3"]:
    fetch(name)
print(f"{time.perf_counter() - start:.1f}초")
