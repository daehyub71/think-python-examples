# 생각하는 파이썬 Part 3 · while True
# (강의 슬라이드: 일부러 만드는 무한 반복)

while True:
    command = input("명령(quit 으로 종료) > ")
    if command == "quit":
        print("종료합니다.")
        break               # 나가는 문을 반드시 마련해 둔다
    print(f"실행: {command}")
