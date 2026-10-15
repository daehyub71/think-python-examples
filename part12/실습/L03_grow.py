import timeit

for size in [1_000, 10_000, 100_000]:
    ids = list(range(size))
    id_set = set(ids)
    last = size - 1                       # 맨 끝의 값을 찾는다
    t_list = min(timeit.repeat(lambda: last in ids, number=200, repeat=5))
    t_set = min(timeit.repeat(lambda: last in id_set, number=200, repeat=5))
    print(f"{size:>7,}개  리스트가 셋보다 {t_list / t_set:,.0f}배 느리다")
