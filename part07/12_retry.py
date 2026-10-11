# 생각하는 파이썬 Part 7 · 실패하면 다시 — retry


import functools
import time

def retry(times, delay=0.1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:                                     # try · except 는 Part 8 에서 배웁니다
                    return func(*args, **kwargs)         # 성공하면 바로 돌려준다
                except ConnectionError as e:
                    print(f"{attempt}번째 실패: {e}")
                    if attempt == times:
                        raise                            # 끝까지 실패하면 오류를 그대로 올린다
                    time.sleep(delay)                    # 잠깐 쉬고 다시
        return wrapper
    return decorator

count = 0

@retry(times=3)
def fetch_rate():                    # 세 번째에야 성공하는 흉내
    global count
    count += 1
    if count < 3:
        raise ConnectionError("응답 없음")
    return 1385.5

print(fetch_rate())
# 1번째 실패: 응답 없음
# 2번째 실패: 응답 없음
# 1385.5
