import timeit

def by_comp():
    return [n * n for n in range(1000)]

def by_loop():
    out = []
    for n in range(1000):
        out.append(n * n)
    return out

def by_map():
    return list(map(lambda n: n * n, range(1000)))

for f in (by_comp, by_loop, by_map):
    best = min(timeit.repeat(f, number=2000, repeat=5))
    print(f"{f.__name__:8} {best / 2000 * 1e6:6.1f}µs")
