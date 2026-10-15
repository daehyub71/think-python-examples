import timeit

ids = list(range(5_000))
id_set = set(ids)                 # 한 번만 바꿔 둔다

def count_list():
    return sum(1 for n in range(0, 10_000, 2) if n in ids)

def count_set():
    return sum(1 for n in range(0, 10_000, 2) if n in id_set)

print(count_list(), count_set())  # 답은 같다
t_list = min(timeit.repeat(count_list, number=10, repeat=5))
t_set = min(timeit.repeat(count_set, number=10, repeat=5))
print(f"리스트 {t_list / 10 * 1000:.2f}ms")
print(f"셋     {t_set / 10 * 1000:.3f}ms")
