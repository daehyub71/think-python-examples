# 생각하는 파이썬 Part 10 · 직접 해보기 풀이
# 실행: python3 practice_answers.py   (같은 폴더의 work.py 를 씁니다. 시간은 컴퓨터마다 다릅니다)

import threading
import time
from multiprocessing import Pool
from work import crunch


def slow_job(number):
    time.sleep(2)                    # 2초씩 걸리는 "기다리는 일"


def run_threads(func, values):
    """values 의 값마다 스레드를 하나씩 만들어 func(값) 을 시키고, 모두 끝날 때까지 기다린다."""
    threads = []
    for v in values:
        t = threading.Thread(target=func, args=(v,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


if __name__ == "__main__":
    # ① 기다림 겹치기 ------------------------------------------------------
    start = time.perf_counter()
    for i in range(5):
        slow_job(i)
    print(f"① 순서대로 {time.perf_counter() - start:.1f}초")      # 10.0초 (2초 × 5)

    start = time.perf_counter()
    run_threads(slow_job, range(5))
    print(f"① 스레드로 {time.perf_counter() - start:.1f}초")      # 2.0초 — 다섯 번의 기다림이 겹친다

    # ② start 대신 run ---------------------------------------------------
    start = time.perf_counter()
    for i in range(5):
        threading.Thread(target=slow_job, args=(i,)).run()        # start() 가 아니라 run()
    print(f"② run 으로 {time.perf_counter() - start:.1f}초")      # 10.0초 — 스레드가 하나도 생기지 않았다
    # run() 은 맡긴 함수를 "지금 이 흐름에서" 그대로 부를 뿐이다. 새 흐름을 만들어 출발시키는 것은 start() 다

    # ③ 자물쇠 걸기 (읽기와 쓰기 사이에 sleep 을 넣어 틈을 벌린다) ----------
    stock = 200

    def take(times):                 # Lock 없이
        global stock
        for _ in range(times):
            now = stock
            time.sleep(0.001)
            stock = now - 1

    run_threads(take, [50] * 4)
    print("③ Lock 없이:", stock)     # 150 — 넷이 같은 값을 읽고 같은 값을 적어, 50번만 줄었다

    stock = 200
    lock = threading.Lock()

    def take_safely(times):          # Lock 을 걸고
        global stock
        for _ in range(times):
            with lock:
                now = stock
                time.sleep(0.001)
                stock = now - 1

    run_threads(take_safely, [50] * 4)
    print("③ Lock 걸고:", stock)     # 0

    # ④ 일꾼 수 바꿔 보기 --------------------------------------------------
    N = 15_000_000
    for workers in (1, 2, 4):
        start = time.perf_counter()
        with Pool(workers) as pool:
            pool.map(crunch, [N] * 4)
        print(f"④ Pool({workers}) {time.perf_counter() - start:.1f}초")
    # 이 컴퓨터(12코어)에서는 2.0초 → 1.0초 → 0.5초쯤. 코어가 넉넉할 때는 거의 절반씩 줄지만,
    # 일꾼을 코어 수보다 늘리면 더 줄지 않고, 일이 작으면 프로세스를 띄우는 시간 때문에 오히려 늘어난다
