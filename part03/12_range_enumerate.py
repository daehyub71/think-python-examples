# 생각하는 파이썬 Part 3 · range 와 enumerate
# (강의 슬라이드: range() · enumerate())

print(list(range(4)))       # [0, 1, 2, 3]
print(list(range(3, 8)))    # [3, 4, 5, 6, 7]  ← 끝 숫자 8 은 포함되지 않는다
print(list(range(1, 11)))   # 1부터 10까지는 range(1, 11)

for i in range(3):          # "세 번 반복"
    print(f"재시도 {i + 1}회...")

# 번호가 필요하면 enumerate() — (번호, 항목) 한 쌍을 건네준다
items = ["노트", "펜", "지우개"]
for no, item in enumerate(items, start=1):
    print(f"{no}번: {item}")
