def exclaim(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"
    return wrapper

def quote(func):
    def wrapper(*args, **kwargs):
        return "「" + func(*args, **kwargs) + "」"
    return wrapper

@exclaim
@quote
def greet(name):
    return f"{name}님 반갑습니다"

print(greet("하늘"))
