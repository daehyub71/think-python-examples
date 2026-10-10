# 생각하는 파이썬 Part 3 · 조건 표현 세 가지
# (강의 슬라이드: 조건을 사람 말처럼 쓰는 세 가지)

# ① in — 들어 있나
email = "skim@company"
if "." not in email:
    print("주소를 확인하세요")

# ② 이어 쓰는 비교
temp = 7
if 0 <= temp <= 30:
    print("정상 보관 온도")

# ③ 한 줄 조건 — "0, 단 100개 이상일 때. 아니면 3000"
qty = 120
fee = 0 if qty >= 100 else 3000
print(fee)                  # 0
