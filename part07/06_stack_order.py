# 생각하는 파이썬 Part 7 · 겹쳐 쓰기 — 함수에 가까운 것부터 감싼다


def exclaim(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"
    return wrapper

def quote(func):
    def wrapper(*args, **kwargs):
        return "「" + func(*args, **kwargs) + "」"
    return wrapper

@quote
@exclaim
def greet(name):                     # greet = quote(exclaim(greet))
    return f"{name}님 반갑습니다"

print(greet("하늘"))                 # 「하늘님 반갑습니다!」

@exclaim
@quote
def greet2(name):                    # greet2 = exclaim(quote(greet2))
    return f"{name}님 반갑습니다"

print(greet2("하늘"))                # 「하늘님 반갑습니다」!
