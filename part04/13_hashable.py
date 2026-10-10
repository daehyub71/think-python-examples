# 생각하는 파이썬 Part 4 · 키와 불변
# (강의 슬라이드: 딕셔너리와 셋은 왜 빨리 찾을까)

treasure = {(2, 3): "보물"}  # 튜플은 키가 될 수 있다
print(treasure[(2, 3)])     # 보물

# 아래 줄은 주석을 풀면 TypeError: unhashable type: 'list'
# bad = {[2, 3]: "보물"}
