import time
from team import run_together    # 스레드를 만들고 기다려 준다 (team.py)

visitors = 0

def enter(times):
    global visitors
    for _ in range(times):
        now = visitors           # 읽고
        time.sleep(0.001)        # (잠깐 다른 일)
        visitors = now + 1       # 하나 더해 적는다

run_together(enter, threads=3, times=100)
print(visitors)
