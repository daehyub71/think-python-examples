# 생각하는 파이썬 Part 3 · or 가 돌려주는 값
# (강의 슬라이드: 판정이 아니라 "고르기")

print("" or "손님")          # 손님 — 왼쪽이 비었으니 오른쪽
print("대협" or "손님")      # 대협 — 왼쪽에 값이 있으니 왼쪽
print(0 or 100)             # 100

# 기본값을 채울 때 자주 쓰는 표현 — 아무것도 치지 않고 Enter 를 누르면 "손님"
nickname = input("별명: ")
name = nickname or "손님"
print(f"{name}님, 환영합니다")
