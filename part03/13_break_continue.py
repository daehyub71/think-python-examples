# 생각하는 파이썬 Part 3 · break 와 continue
# (강의 슬라이드: break 와 continue)

stocks = [12, 45, 0, 33, 7]
for qty in stocks:
    if qty == 0:
        print("품절 발견! 중단")
        break               # 반복을 완전히 빠져나간다 — 33과 7은 보지도 않는다
    print(f"정상: {qty}개")

temps = [21, -999, 23, -999, 25]    # -999 는 온도계가 고장 났을 때 찍히는 값
for t in temps:
    if t == -999:
        continue            # 이번 바퀴만 건너뛰고 계속 돈다
    print(f"유효: {t}도")
