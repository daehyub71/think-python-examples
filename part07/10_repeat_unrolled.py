# 생각하는 파이썬 Part 7 · @repeat(3) 을 손으로 풀어 쓰면 두 단계


import functools

def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

def cheer(team):
    print(f"{team} 화이팅")

deco = repeat(2)                     # ① 괄호가 먼저 실행된다 — "2번짜리 데코레이터"가 나온다
cheer = deco(cheer)                  # ② 그 데코레이터로 함수를 감싼다

cheer("백팀")
# 백팀 화이팅
# 백팀 화이팅
