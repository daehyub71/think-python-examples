import functools

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} 호출")
        return func(*args, **kwargs)
    return wrapper

@log_call
def to_won(amount):
    """숫자를 원 단위 글자로 바꾼다."""
    return f"{amount:,}원"

print(to_won.__name__)
print(to_won.__doc__)
print(to_won.__wrapped__(12500))
