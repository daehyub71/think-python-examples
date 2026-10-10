# 생각하는 파이썬 Part 3 · elif 와 else
# (강의 슬라이드: 갈래가 여럿일 때)

score = 83                  # 89, 90, 70, 69 를 넣어 경계를 확인해 보세요

if score >= 90:
    grade = "A"
elif score >= 80:           # "그게 아니고, 만약"
    grade = "B"
elif score >= 70:
    grade = "C"
else:                       # "전부 아니면"
    grade = "F"
print(f"점수 {score} → 등급 {grade}")     # 점수 83 → 등급 B

# 위에서부터 검사해 처음 참인 갈래 하나만 실행합니다.
