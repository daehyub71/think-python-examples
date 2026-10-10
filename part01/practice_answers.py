# 생각하는 파이썬 Part 1 · 실습 풀이
# (강의 슬라이드: 직접 해보기)


# ① 창고 한 칸 — 변수 네 개와 타입
name = "무선 마우스"
stock = 1200
price = 3500.0
sold_out = False
print(type(name), type(stock), type(price), type(sold_out))

# ② 시간 바꾸기 — 137분은 몇 시간 몇 분?
minutes = 137
print(minutes // 60, "시간", minutes % 60, "분")      # 2 시간 17 분

# ③ 입력 두 번 받아 더하기 (고친 버전 — 틀린 버전은 12_input_trap.py)
first = int(input("첫째 수: "))
second = int(input("둘째 수: "))
print(first + second)

# ④ 달성률 — 목표 1000, 실적 873 을 넣으면 87.3%
target = int(input("목표량: "))
actual = int(input("실적: "))
print(f"달성률: {actual / target:.1%}")
