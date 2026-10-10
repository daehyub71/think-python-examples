# 생각하는 파이썬 Part 5 · 위치 인자와 키워드 인자


def reserve(name, day, people):
    return f"{name}님 {day} {people}명"

print(reserve("이서준", "토요일", 4))                    # 위치 인자 — 순서가 곧 뜻
print(reserve(people=4, name="이서준", day="토요일"))    # 키워드 인자 — 순서가 바뀌어도 된다
print(reserve("이서준", people=4, day="토요일"))         # 섞을 때는 위치 인자가 먼저
# reserve(name="이서준", "토요일", 4)   # SyntaxError: positional argument follows keyword argument
