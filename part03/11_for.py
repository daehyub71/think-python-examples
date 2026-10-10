# 생각하는 파이썬 Part 3 · for
# (강의 슬라이드: for — 묶음에서 하나씩 꺼낸다)

items = ["노트", "펜", "지우개"]
for item in items:
    print(f"오늘 입고: {item}")

# 문자열도 묶음 — 한 글자씩 나온다
for ch in "파이썬":
    print(ch, end=" ")
print()
