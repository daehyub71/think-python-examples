# 생각하는 파이썬 Part 1 · input 의 함정
# (강의 슬라이드: input() 으로 받은 두 수를 더하면?)


# 3 과 5 를 넣어 보세요. 8 이 아니라 35 가 나옵니다.
first = input("첫째 수: ")
second = input("둘째 수: ")
print(first + second)       # input() 이 돌려주는 값은 언제나 문자열 — "3" + "5" = "35"
