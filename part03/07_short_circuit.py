# 생각하는 파이썬 Part 3 · 단락 평가
# (강의 슬라이드: and 와 or · 안전장치)

total = 0
count = 0                   # 응시자가 아직 한 명도 없다

# print(total / count >= 80)     # 주석을 풀면 ZeroDivisionError: division by zero

# 앞에 확인을 하나 세웁니다. 왼쪽이 거짓이면 오른쪽은 실행조차 되지 않습니다.
print(count > 0 and total / count >= 80)      # False

total = 255
count = 3
print(count > 0 and total / count >= 80)      # True (평균 85)
