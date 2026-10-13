# 생각하는 파이썬 Part 8 · 직접 해보기 풀이


import csv
import json

# ① 글자를 숫자로, 안 되면 None -------------------------------------------
def to_float(text):
    try:
        return float(text)
    except ValueError:               # 바꿀 수 없는 글자면 멈추지 않고 None
        return None

print(to_float("36.5"))              # 36.5
print(to_float("미열"))              # None

# ② 범위를 벗어나면 raise -------------------------------------------------
def pick(number):
    if number < 1 or number > 45:    # 가드 절 — 잘못된 값은 입구에서 막는다
        raise ValueError(f"1~45 사이의 번호만 고를 수 있습니다: {number}")
    return f"{number}번 선택"

print(pick(7))                       # 7번 선택
try:
    print(pick(50))
except ValueError as e:
    print("고르지 못함 →", e)        # 고르지 못함 → 1~45 사이의 번호만 고를 수 있습니다: 50

# (더 해 보기) 내 예외로 바꾸기
class OutOfRangeError(Exception):
    def __init__(self, number):
        super().__init__(f"{number} 은 1~45 밖입니다")
        self.number = number

def pick2(number):
    if number < 1 or number > 45:
        raise OutOfRangeError(number)
    return f"{number}번 선택"

try:
    pick2(0)
except OutOfRangeError as e:
    print(e, "/ 넣은 값:", e.number)  # 0 은 1~45 밖입니다 / 넣은 값: 0

# ③ 줄 수와 글자 수 세기 --------------------------------------------------
def count(path):
    lines = 0
    chars = 0
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:                   # 한 줄씩 읽는다
                lines += 1
                chars += len(line.strip())   # 줄 끝의 \n 은 빼고 센다
    except FileNotFoundError:
        print(f"{path} 파일이 없습니다")
        return None
    return lines, chars

with open("memo.txt", "w", encoding="utf-8") as f:
    f.write("오늘은 공원을 걸었다\n내일은 강변\n")

print(count("memo.txt"))             # (2, 17)
print(count("없는파일.txt"))         # 없는파일.txt 파일이 없습니다 / None

# ④ CSV 를 JSON 으로 ------------------------------------------------------
with open("walks.csv", "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows([["요일", "코스", "걸음"], ["월", "공원", 6200], ["화", "강변", 8450], ["수", "공원", 7300]])

totals = {}
with open("walks.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        totals[row["코스"]] = totals.get(row["코스"], 0) + int(row["걸음"])   # 읽은 값은 문자열 → int()

with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(totals, f, ensure_ascii=False, indent=2)

with open("summary.json", encoding="utf-8") as f:
    print(json.load(f))              # {'공원': 13500, '강변': 8450}
