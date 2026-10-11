def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} 호출")
        result = func(*args, **kwargs)
        return result
    return wrapper()

@log_call
def discount(price, rate=0.1):
    return round(price * (1 - rate))

print(discount(20000, rate=0.25))
