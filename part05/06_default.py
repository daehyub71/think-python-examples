# 생각하는 파이썬 Part 5 · 기본값 인자


def order(menu, size="중", ice=True):
    return f"{menu} / {size} / {'얼음' if ice else '따뜻하게'}"

print(order("라떼"))                # 라떼 / 중 / 얼음
print(order("라떼", "대"))          # 라떼 / 대 / 얼음
print(order("라떼", ice=False))     # 라떼 / 중 / 따뜻하게
# def bad(size="중", menu): ...     # SyntaxError — 기본값이 있는 매개변수는 뒤에
