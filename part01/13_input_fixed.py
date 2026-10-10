# 생각하는 파이썬 Part 1 · input 고친 버전
# (강의 슬라이드: 해결 — 받자마자 숫자로 바꾼다)


first = int(input("첫째 수: "))
second = int(input("둘째 수: "))
print(first + second)       # 3 과 5 를 넣으면 8

# 숫자가 아닌 것(예: 3.5, abc)을 넣으면 ValueError 가 납니다.
# 소수를 받으려면 float(input(...)) 을 씁니다.
