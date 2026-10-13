# 생각하는 파이썬 Part 9 · 직접 해보기 풀이
# 검사: mypy practice_answers.py  →  Success (맨 아래 "일부러 틀린 줄"의 주석을 풀면 오류가 나옵니다)

from typing import Literal, Protocol

# ① 힌트를 붙이고 검사하기 -----------------------------------------------
def area(width: float, height: float) -> float:
    return width * height

print(area(3, 4.5))                  # 13.5
# print(area("3", 4.5))              # mypy: Argument 1 to "area" has incompatible type "str"; expected "float"

# ② 없을 수도 있는 값 -----------------------------------------------------
def longest(words: list[str]) -> str | None:
    if not words:                    # 빈 목록이면 None
        return None
    return max(words, key=len)

word = longest(["사과", "파인애플", "배"])
if word is None:                     # 먼저 확인한다
    print("단어가 없습니다")
else:
    print(word.upper(), len(word))   # 파인애플 4
# print(longest([]).upper())         # mypy: Item "None" of "str | None" has no attribute "upper"

# ③ 정해진 값만 받기 ------------------------------------------------------
def ticket(day: Literal["평일", "주말"]) -> int:
    return {"평일": 9000, "주말": 12000}[day]

print(ticket("주말"))                # 12000
# print(ticket("공휴일"))            # mypy: … incompatible type "Literal['공휴일']"; expected "Literal['평일', '주말']"
#                                    # 힌트 없이 실행했다면 KeyError: '공휴일' 로 멈춘다

# ④ 상속 없이 약속하기 ----------------------------------------------------
class Labeled(Protocol):
    def label(self) -> str: ...

class Parcel:                        # Labeled 를 상속하지 않았다
    def label(self) -> str:
        return "택배 #1024"

class Jar:
    def label(self) -> str:
        return "매실청 2026"

class Stone:
    pass

def stick(item: Labeled) -> None:
    print(f"[{item.label()}]")

stick(Parcel())                      # [택배 #1024]
stick(Jar())                         # [매실청 2026]
# stick(Stone())                     # mypy: Argument 1 to "stick" has incompatible type "Stone"; expected "Labeled"
