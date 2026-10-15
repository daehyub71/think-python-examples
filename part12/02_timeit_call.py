import timeit

def make_squares():
    return [n * n for n in range(1000)]

total = timeit.timeit(make_squares, number=10_000)
print(f"1만 번 전체 {total:.3f}초")
print(f"한 번에 {total / 10_000 * 1e6:.1f}µs")

times = timeit.repeat(make_squares, number=10_000, repeat=5)
print([round(t, 3) for t in times])
print(f"가장 빠른 기록 {min(times):.3f}초")
