# 생각하는 파이썬 Part 2 · AST 나무
# (강의 슬라이드: AST · ast 모듈)


import ast                  # 파이썬에 들어 있는 도구 상자를 꺼내 온다

# 곱셈(Mult)이 덧셈(Add)의 안쪽에 들어 있습니다 — 먼저 계산된다는 뜻
print(ast.dump(ast.parse("pay = 8 + 4 * 5"), indent=4))

# 괄호를 넣으면 나무 모양이 바뀝니다 — 이번에는 덧셈이 안쪽
print(ast.dump(ast.parse("pay = (8 + 4) * 5"), indent=4))

# 나무를 다시 코드로 — 들쭉날쭉한 띄어쓰기가 가지런해진다
tree = ast.parse("x=( 8+4 )*5")
print(ast.unparse(tree))    # x = (8 + 4) * 5
