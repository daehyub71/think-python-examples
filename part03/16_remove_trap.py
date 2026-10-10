# 생각하는 파이썬 Part 3 · 순회 중 수정
# (강의 슬라이드: 돌면서 지우지 않는다)

# 짝수를 전부 지우려 했다 — 5 만 남아야 하는데...
numbers = [2, 4, 6, 8, 5]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)
print(numbers)              # [4, 8, 5] ← 4와 8을 건너뛰었다 (오류도 없이)

# 남길 것만 새 리스트에 담는다
numbers = [2, 4, 6, 8, 5]
odds = []
for n in numbers:
    if n % 2 != 0:
        odds.append(n)
print(odds)                 # [5]
