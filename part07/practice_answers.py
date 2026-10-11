# 생각하는 파이썬 Part 7 · 직접 해보기 풀이


import functools

# ① @ 를 손으로 풀어 쓰기 ------------------------------------------------
def ruler(func):
    def wrapper(*args, **kwargs):
        print("-----")
        result = func(*args, **kwargs)
        print("-----")
        return result
    return wrapper

def show_menu(day):
    print(f"{day}요일 메뉴: 비빔밥")

show_menu = ruler(show_menu)         # @ruler 를 붙인 것과 똑같다
show_menu("수")
# -----
# 수요일 메뉴: 비빔밥
# -----

# ② 호출 횟수를 세는 데코레이터 ------------------------------------------
def count_calls(func):
    count = 0                        # wrapper 가 기억해 둘 값(클로저)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count               # 바깥 함수의 count 를 고치겠다는 표시
        count += 1
        print(f"{count}번째 호출")
        return func(*args, **kwargs)
    return wrapper

@count_calls
def ping():
    return "pong"

ping()                               # 1번째 호출
ping()                               # 2번째 호출

# ③ return 을 빼먹으면 ---------------------------------------------------
def forgetful(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)        # 결과를 받아 놓고 돌려주지 않는다
    return wrapper

@forgetful
def add_tax(price):
    return round(price * 1.1)

print(add_tax(10000))                # None — wrapper 가 아무것도 돌려주지 않았기 때문

# ④ 설정값을 받는 데코레이터 @tag ----------------------------------------
def tag(mark):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f"{mark} {func(*args, **kwargs)} {mark}"
        return wrapper
    return decorator

@tag("[중요]")
def notice():
    return "내일은 쉽니다"

print(notice())                      # [중요] 내일은 쉽니다 [중요]
