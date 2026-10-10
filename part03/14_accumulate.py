# 생각하는 파이썬 Part 3 · 누적 패턴
# (강의 슬라이드: 가장 중요한 패턴 · 세기 · 흔한 실수)

sales = [120, 85, 200, 95, 150]

total = 0                   # ① 그릇을 먼저 (반복 밖에서!)
for amount in sales:
    total = total + amount  # ② 바퀴마다 더한다
    print(amount, total)    # 바퀴별 표: 120 / 205 / 405 / 500 / 650
print(f"총 매출: {total}")

# 같은 뼈대로 개수 세기
scores = [88, 45, 92, 30, 71, 59]
pass_count = 0
for score in scores:
    if score >= 60:
        pass_count += 1     # pass_count = pass_count + 1 의 줄임
print(f"합격자: {pass_count}명")      # 3명

# 흔한 실수 — 그릇을 반복 안에 두면 바퀴마다 0으로 되돌아간다
for amount in sales:
    total = 0
    total += amount
print(total)                # 150 (650 이 아니다)
