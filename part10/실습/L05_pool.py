import time
from multiprocessing import Pool
from work import crunch

N = 15_000_000
if __name__ == "__main__":
    start = time.perf_counter()
    for _ in range(6):
        crunch(N)
    print(f"순서대로 {time.perf_counter() - start:.3f}초")

    start = time.perf_counter()
    with Pool(3) as pool:
        results = pool.map(crunch, [N] * 6)
    print(f"일꾼 셋  {time.perf_counter() - start:.3f}초")

# 영상의 마지막 단계에서는 N 을 1_000 으로 줄여, 나눠 준 쪽이 오히려 오래 걸리는 것을 보였습니다.
