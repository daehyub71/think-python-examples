# 생각하는 파이썬 Part 3 · 조건의 순서
# (강의 슬라이드: 순서가 곧 논리다)

# 오류 메시지는 없지만 답이 틀립니다(의미 오류).
score = 95
if score >= 60:             # 95 는 60 이상이기도 하다 → 여기서 걸리고 끝
    grade = "D"
elif score >= 70:
    grade = "C"
elif score >= 90:
    grade = "A"
print(grade)                # D

# 좁은 조건을 위에, 넓은 조건을 아래에 두어야 합니다. 순서를 고쳐 보세요.
