# 생각하는 파이썬 Part 7 · 이미 만들어져 있는 데코레이터 — functools.cache


from functools import cache

calls = 0

def ways(n):                         # 계단 n칸을 한 번에 1칸 또는 2칸씩 오르는 방법의 수
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways(n - 1) + ways(n - 2)

print(ways(25), calls)               # 121393 242785 — 같은 계산을 24만 번 넘게 했다

calls = 0

@cache                               # 한 번 구한 답은 적어 두고 다시 쓴다
def ways(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways(n - 1) + ways(n - 2)

print(ways(25), calls)               # 121393 26 — 칸 수마다 딱 한 번씩만 계산했다
print(ways.cache_info())             # CacheInfo(hits=23, misses=26, maxsize=None, currsize=26)
