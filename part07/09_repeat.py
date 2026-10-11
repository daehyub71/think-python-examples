# 생각하는 파이썬 Part 7 · 설정값을 받는 데코레이터 — 세 겹


import functools

def repeat(times):                           # ① 설정값을 받는다
    def decorator(func):                     # ② 함수를 받는다 — 여기부터는 늘 보던 데코레이터
        @functools.wraps(func)
        def wrapper(*args, **kwargs):        # ③ 실제 호출을 받는다
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def cheer(team):
    print(f"{team} 화이팅")

cheer("청팀")
# 청팀 화이팅
# 청팀 화이팅
# 청팀 화이팅
