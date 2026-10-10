# 생각하는 파이썬 Part 3 · 실습 풀이
# (강의 슬라이드: 직접 해보기)

# ① 은 03_elif_else.py 의 score 를 89, 90, 70, 69 로 바꿔 실행 → B, A, C, F
# ② 는 05_truthy_falsy.py 의 마지막 반복문

# ③ 근무시간 집계
hours = [8, 9, 7, 8, 10]
total = 0
over = 0
for h in hours:
    total += h
    if h > 8:
        over += 1
print("총합:", total)                   # 42
print("하루 평균:", total / len(hours))  # 8.4
print("8시간 넘긴 날:", over)            # 2

# ④ 섭씨를 화씨로 — 컴프리헨션 한 줄
celsius = [0, 18, 25, 30, 37]
fahrenheit = [c * 9 / 5 + 32 for c in celsius]
print(fahrenheit)                       # [32.0, 64.4, 77.0, 86.0, 98.6]
