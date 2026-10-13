import time
from multiprocessing import Pool
from work import crunch

N = 15_000_000
if __name__ == "__main__":
    start = time.perf_counter()
    for _ in range(6):
        crunch(N)
    print(f"순서대로 {time.perf_counter() - start:.1f}초")

    start = time.perf_counter()
    with Pool(3) as pool:                    # 일꾼 프로세스 셋
        results = pool.map(crunch, [N] * 6)  # 일감 여섯 개
    print(f"일꾼 셋  {time.perf_counter() - start:.1f}초")
