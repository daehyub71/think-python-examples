# 생각하는 파이썬 Part 5 · for 의 속 — iter() 와 next()


it = iter(["월", "화", "수"])
print(next(it))                     # 월
print(next(it))                     # 화
print(next(it))                     # 수
# print(next(it))                   # 주석을 풀면 StopIteration

# for 가 안에서 하는 일
it = iter(["월", "화", "수"])
while True:
    try:
        day = next(it)
    except StopIteration:
        break
    print(day)
