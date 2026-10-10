# 생각하는 파이썬 Part 4 · 리스트 대 셋 속도
# (강의 슬라이드: 같은 질문, 수만 배의 차이)

import time

allowed_list = list(range(1_000_000))
allowed_set = set(range(1_000_000))
target = 999_999

start = time.perf_counter()
for _ in range(100):
    target in allowed_list              # 처음부터 하나씩 본다
t_list = time.perf_counter() - start

start = time.perf_counter()
for _ in range(100):
    target in allowed_set               # 그 칸으로 곧장 간다
t_set = time.perf_counter() - start

print(f"리스트: {t_list:.4f}초")
print(f"셋:    {t_set:.7f}초")
print(f"약 {t_list / t_set:,.0f}배")     # 컴퓨터와 실행할 때마다 다르지만 수만 배 이상
