# 생각하는 파이썬 Part 5 · yield — 멈췄다가 이어 달리는 함수


import sys

def tickets(n):
    print("발권 시작")
    for i in range(1, n + 1):
        yield i                     # 하나 내놓고 멈춘다
    print("매진")

g = tickets(2)                      # 아직 아무것도 실행되지 않는다
print(next(g))                      # 발권 시작 / 1
print(next(g))                      # 2
print(list(g))                      # 매진 / []

big_list = [n * 3 for n in range(500_000)]
big_gen = (n * 3 for n in range(500_000))
print(sys.getsizeof(big_list))      # 약 417만 바이트
print(sys.getsizeof(big_gen))       # 200 바이트 안팎

gen = (x * x for x in range(5))
print(sum(gen))                     # 30
print(sum(gen))                     # 0 — 한 번 쓰면 끝
