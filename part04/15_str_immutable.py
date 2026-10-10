# 생각하는 파이썬 Part 4 · 문자열 불변
# (강의 슬라이드: 문자열은 바뀌지 않는다)

s = "python"
# s[0] = "P"                # 주석을 풀면 TypeError: 'str' object does not support item assignment
s = "P" + s[1:]             # 새 문자열을 만들어 이름표를 옮긴다
print(s)                    # Python

t = "hello"
t.upper()                   # 결과를 받지 않으면 사라진다
print(t)                    # hello ← 원본은 그대로
t = t.upper()               # 다시 받아야 남는다
print(t)                    # HELLO
