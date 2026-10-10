# 생각하는 파이썬 Part 2 · 객체
# (강의 슬라이드: 파이썬에서 모든 값은 객체다)


x = 3
print(type(x))              # <class 'int'>
print(id(x))                # 고유 번호 — 실행할 때마다 달라집니다
print(type(type(x)))        # <class 'type'> — 타입조차 객체
