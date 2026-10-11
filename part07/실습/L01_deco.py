def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} 호출")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_call
def discount(price, rate=0.1):
    return round(price * (1 - rate))

print(discount(20000, rate=0.25))

# 영상의 마지막 단계에서는 6번 줄을 return wrapper() 로 바꿔 일부러 오류를 냈습니다.
# 괄호를 붙이면 @log_call 줄에서 wrapper 가 그 자리에서 실행되어 TypeError 가 납니다.
