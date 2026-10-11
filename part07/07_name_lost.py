# 생각하는 파이썬 Part 7 · 감쌌더니 이름과 설명이 사라졌다


def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} 호출")
        return func(*args, **kwargs)
    return wrapper

@log_call
def to_won(amount):
    """숫자를 원 단위 글자로 바꾼다."""
    return f"{amount:,}원"

print(to_won(12500))                 # to_won 호출 / 12,500원 — 동작은 멀쩡하다
print(to_won.__name__)               # wrapper  ← to_won 이 아니다
print(to_won.__doc__)                # None     ← 설명도 사라졌다
