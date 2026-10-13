# 생각하는 파이썬 Part 11 · 직접 해보기 풀이
# 실행: python3 practice_answers.py   (같은 폴더의 scoreboard.py · red_team.py · blue_team.py 를 씁니다)

import csv
import json

# ① 함께 쓰는 점수판 ------------------------------------------------------
import red_team
import blue_team
from scoreboard import board

red_team.score()                     # red_team.py 에서 3점
blue_team.score()                    # blue_team.py 에서 2점
print("①", board.points)             # 5 — 두 파일이 같은 점수판에 더했다

# ② 저장기 팩토리 ---------------------------------------------------------
class TxtSaver:
    def save(self, rows, path):
        with open(path, "w", encoding="utf-8") as f:
            for row in rows:
                f.write(" ".join(str(v) for v in row) + "\n")

class CsvSaver:
    def save(self, rows, path):
        with open(path, "w", encoding="utf-8", newline="") as f:
            csv.writer(f).writerows(rows)

class JsonSaver:
    def save(self, rows, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)

SAVERS = {"txt": TxtSaver, "csv": CsvSaver, "json": JsonSaver}

def make_saver(kind):
    if kind not in SAVERS:
        raise ValueError(f"모르는 저장 형식: {kind}")
    return SAVERS[kind]()            # 클래스를 꺼내서 만든다

rows = [["월", 6200], ["화", 8450]]
for kind in ["txt", "csv", "json"]:
    make_saver(kind).save(rows, f"walk.{kind}")     # 종류가 달라도 쓰는 법은 같다
    print("②", f"walk.{kind} 저장")
try:
    make_saver("xlsx")
except ValueError as e:
    print("②", e)                    # 모르는 저장 형식: xlsx

# ③ 배송비 전략 -----------------------------------------------------------
def basic(weight):                   # 기본: 3000원 + 1kg 마다 500원
    return 3000 + weight * 500

def express(weight):                 # 빠른 배송: 기본의 두 배
    return basic(weight) * 2

def free(weight):                    # 무료 배송
    return 0

def shipping(weight, rule=basic):    # 본문은 규칙을 받아서 부를 뿐이다
    return rule(weight)

print("③", shipping(4), shipping(4, express), shipping(4, free))    # 5000 10000 0

# ④ 이미 있는 전략 찾기 ---------------------------------------------------
words = ["감", "파인애플", "배", "한라봉", "귤"]
print("④", max(words, key=len))      # 파인애플 — 길이를 기준으로
print("④", max(words))               # 한라봉   — 기준을 안 주면 글자(사전) 순서
print("④", min(words, key=len))      # 감       — 길이가 같으면 먼저 나온 것
