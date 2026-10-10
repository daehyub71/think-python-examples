# 생각하는 파이썬 Part 5 · 함수 안의 이름표는 안에서만 산다


def box_fee(weight):
    extra = weight * 500            # extra 는 함수 안에서만 사는 이름표
    return 3000 + extra

print(box_fee(4))                   # 5000
# print(extra)                      # 주석을 풀면 NameError: name 'extra' is not defined

# 함수 밖의 값을 바꾸고 싶으면 — 받아서, 돌려준다
def visit(n):
    return n + 1

visits = 0
visits = visit(visits)
visits = visit(visits)
print(visits)                       # 2
