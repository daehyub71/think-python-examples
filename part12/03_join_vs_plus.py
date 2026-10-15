import timeit

lines = [f"주문-{i}" for i in range(20_000)]

def by_plus():
    text = ""
    for line in lines:
        text += line + "\n"     # 줄마다 붙인다
    return text

def by_join():
    return "\n".join(lines) + "\n"   # 길이를 재고 한 번에

print(by_plus() == by_join())
t_plus = min(timeit.repeat(by_plus, number=50, repeat=5))
t_join = min(timeit.repeat(by_join, number=50, repeat=5))
print(f"+=   {t_plus / 50 * 1000:.2f}ms")
print(f"join {t_join / 50 * 1000:.2f}ms")
