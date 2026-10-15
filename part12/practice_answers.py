# 생각하는 파이썬 Part 12 · 직접 해보기 풀이
# 실행: python3 practice_answers.py
# 시간 값은 컴퓨터와 실행할 때마다 달라집니다. 숫자보다 "어느 쪽이 몇 배쯤"을 보세요.

import cProfile
import os
import tempfile
import timeit
import tracemalloc

def best(func, number):
    """repeat 다섯 번 중 가장 빠른 기록을, 한 번에 걸린 마이크로초로"""
    return min(timeit.repeat(func, number=number, repeat=5)) / number * 1e6

# ① 글자 끼워 넣기 세 가지 -------------------------------------------------
name, age = "하늘", 27
ways = {
    "f-string": lambda: f"{name}님은 {age}살입니다",
    "format  ": lambda: "{}님은 {}살입니다".format(name, age),
    "%       ": lambda: "%s님은 %d살입니다" % (name, age),
}
print("① 글자 끼워 넣기")
for label, func in ways.items():
    print(f"   {label} {best(func, 200_000):.3f}µs")
# 보통 f-string 이 가장 빠르고, 나머지 둘은 비슷합니다. 하지만 셋 다 0.1µs 안팎 —
# 한두 번 쓰는 자리라면 읽기 쉬운 쪽(f-string)을 고르면 됩니다.

# ② 더하기 두 방법 ---------------------------------------------------------
def add_loop(nums):
    total = 0
    for n in nums:
        total += n
    return total

print("② 더하기 두 방법")
for size in [10_000, 1_000_000]:
    nums = list(range(size))
    t_loop = best(lambda: add_loop(nums), 20)
    t_sum = best(lambda: sum(nums), 20)
    print(f"   {size:>9,}개  반복문 {t_loop:,.0f}µs · sum {t_sum:,.0f}µs · {t_loop / t_sum:.1f}배")
# sum 은 반복을 C 로 된 내부에서 하니 몇 배 빠르고, 개수가 바뀌어도 배수는 비슷합니다.
# (리스트와 셋 찾기처럼 배수가 커지지 않는다 — 둘 다 개수만큼 더하기 때문)

# ③ 숨은 범인 잡기 ---------------------------------------------------------
orders = [f"손님{(n * 7) % 500:03d}" for n in range(2000)]

def load_regulars():
    """단골 명단을 만든다 — 실제로는 파일이나 DB 에서 읽어 오는 일이라 치자"""
    return {f"손님{n:03d}" for n in range(0, 500, 3)}

def count_regulars(orders):
    hits = 0
    for name in orders:
        if name in load_regulars():      # 주문마다 명단을 새로 만든다 ← 범인
            hits += 1
    return hits

def count_regulars_fixed(orders):
    regulars = load_regulars()           # 한 번만 만든다
    return sum(1 for name in orders if name in regulars)

print("③ 숨은 범인 잡기 — 고치기 전 (load_regulars 가 2000번 불리고 시간을 거의 다 쓴다)")
cProfile.run("count_regulars(orders)", sort="tottime")
print("③ 고친 뒤 — load_regulars 1번")
cProfile.run("count_regulars_fixed(orders)", sort="tottime")
print("   답이 같은가:", count_regulars(orders) == count_regulars_fixed(orders))

# ④ 파일을 읽는 두 방법 ----------------------------------------------------
path = os.path.join(tempfile.mkdtemp(), "visits.log")
with open(path, "w", encoding="utf-8") as f:
    for n in range(300_000):
        f.write(f"2026-10-15 방문 {n:06d}\n")

def peak_mb(func):
    tracemalloc.start()
    func()
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return peak / 1024 / 1024

def read_all():
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()            # 30만 줄을 한꺼번에 리스트로
    return sum(1 for line in lines if line.endswith("7\n"))

def read_each():
    with open(path, encoding="utf-8") as f:
        return sum(1 for line in f if line.endswith("7\n"))   # 한 줄씩 흘려보낸다

print("④ 파일 읽기")
print(f"   readlines()      최고 {peak_mb(read_all):.1f}MB")
print(f"   for line in f    최고 {peak_mb(read_each):.2f}MB")
os.remove(path)
