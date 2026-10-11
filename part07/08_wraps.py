# 생각하는 파이썬 Part 7 · functools.wraps — 이름과 설명을 겉으로 옮겨 준다


import functools

def log_call(func):
    @functools.wraps(func)           # ← 이 한 줄
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} 호출")
        return func(*args, **kwargs)
    return wrapper

@log_call
def to_won(amount):
    """숫자를 원 단위 글자로 바꾼다."""
    return f"{amount:,}원"

print(to_won.__name__)               # to_won
print(to_won.__doc__)                # 숫자를 원 단위 글자로 바꾼다.
print(to_won.__wrapped__(12500))     # 12,500원 — 감싸기 전의 원래 함수(로그 없이)
