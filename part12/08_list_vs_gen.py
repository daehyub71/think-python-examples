import tracemalloc

def peak_mb(func):
    tracemalloc.start()
    result = func()
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return result, round(peak / 1024 / 1024, 2)

def with_list():
    return sum([n * n for n in range(2_000_000)])

def with_gen():
    return sum(n * n for n in range(2_000_000))

print("리스트    ", peak_mb(with_list))
print("제너레이터", peak_mb(with_gen))
