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

deco = repeat(2)
cheer = deco(cheer)
cheer("백팀")
