# 생각하는 파이썬 Part 5 · 직접 해보기 풀이


# ① print 와 return
def calc_bmi(height, weight):
    """키(m)와 몸무게(kg)로 체질량지수를 돌려준다."""
    return weight / (height ** 2)

def print_bmi(height, weight):
    print(weight / (height ** 2))

x = calc_bmi(1.75, 70)
print(round(x, 1))                  # 22.9 — 돌려받은 값으로 계속 계산할 수 있다
y = print_bmi(1.75, 70)             # 화면에 22.857142857142858
print(y)                            # None — 출력만 했고 돌려준 것이 없다

# ② 함정 재현하고 고치기
def add_memo(text, memos=[]):
    memos.append(text)
    return memos

add_memo("우유"); add_memo("빵")
print(add_memo("달걀"))             # ['우유', '빵', '달걀'] — 쌓였다
print(add_memo.__defaults__)        # (['우유', '빵', '달걀'],)

def add_memo_ok(text, memos=None):
    if memos is None:
        memos = []
    memos.append(text)
    return memos

add_memo_ok("우유"); add_memo_ok("빵")
print(add_memo_ok("달걀"))          # ['달걀'] — 부를 때마다 새로

# ③ 두 가지 기준으로 정렬 — 연도 최신순, 같은 해면 제목 가나다순
books = [
    {"title": "파이썬 입문", "year": 2021},
    {"title": "알고리즘", "year": 2023},
    {"title": "네트워크", "year": 2021},
    {"title": "운영체제", "year": 2023},
]
for b in sorted(books, key=lambda b: (-b["year"], b["title"])):
    print(b["year"], b["title"])    # 2023 알고리즘 / 2023 운영체제 / 2021 네트워크 / 2021 파이썬 입문

# ④ 내 모듈 만들기 — 아래 두 파일을 같은 폴더에 만든다
# calc.py
#     def add(a, b):
#         return a + b
#     def sub(a, b):
#         return a - b
#     if __name__ == "__main__":
#         print("시험:", add(10, 20))
# use.py
#     import calc
#     print(calc.add(3, 4), calc.sub(9, 5))
# python3 calc.py → "시험: 30" 이 나온다 (직접 실행 → __name__ 이 "__main__")
# python3 use.py  → "7 4" 만 나온다 (import → calc 의 __name__ 은 "calc" 라서 시험 줄을 건너뛴다)
