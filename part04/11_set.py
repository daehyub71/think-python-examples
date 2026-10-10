# 생각하는 파이썬 Part 4 · 셋
# (강의 슬라이드: 셋(set · 집합))

ids = ["park", "kim", "kim", "lee", "park", "kim"]   # 방문 기록 6건
print(len(ids))             # 6
print(len(set(ids)))        # 3 — 실제 방문자 수
print(sorted(set(ids)))     # ['kim', 'lee', 'park'] — 셋에는 순서가 없어 정렬해서 보여 준다

print(type({"kim", "lee"})) # <class 'set'>
print(type({}))             # <class 'dict'> ← 빈 중괄호는 빈 딕셔너리
print(type(set()))          # <class 'set'>  — 빈 셋은 set()
