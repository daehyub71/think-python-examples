# L07_rate.py 가 불러다 쓰는 파일입니다. 같은 폴더에 두세요.
import functools
import time

def retry(times, delay=0.1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except ConnectionError as e:
                    print(f"{attempt}번째 실패: {e}")
                    if attempt == times:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator
