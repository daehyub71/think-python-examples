from functools import cache

calls = 0

@cache
def ways(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways(n - 1) + ways(n - 2)

print(ways(25), calls)
print(ways.cache_info())
