# 생각하는 파이썬 Part 3 · while
# (강의 슬라이드: while — 검사하고, 실행하고, 다시 검사)

# 매주 3,000원씩, 만 원을 채울 때까지
saved = 0
while saved < 10000:
    saved = saved + 3000    # 이 줄을 빼먹으면 무한 루프! (멈출 때는 Ctrl + C)
    print(saved)
print("목표 달성!")
