# 생각하는 파이썬 Part 2 · 실습 풀이
# (강의 슬라이드: 직접 해보기)


import ast
import dis

# ① 은 터미널에서: python3 -m py_compile stock.py  → __pycache__ 의 파일 이름에서 버전 읽기

# ② 괄호가 들어간 식의 나무 — Add 가 Mult 의 안쪽(right)에 들어 있다
print(ast.dump(ast.parse("3 * (4 + 5)"), indent=4))

# ③ 미리 계산해 두는 번역기 — 곱셈 명령은 없고 10080 이 바로 나온다
def week():
    return 7 * 24 * 60

dis.dis(week)
print(week())                   # 10080

# ④ 는 12_pass_to_function.py 와 같습니다.
