# 생각하는 파이썬 Part 4 · 튜플
# (강의 슬라이드: 튜플 — 바뀌지 않는 묶음)

point = (37.5, 127.0)       # 위도, 경도
print(point[0])             # 37.5 — 읽기는 리스트와 같다

# point[0] = 38.0           # 주석을 풀면 TypeError: 'tuple' object does not support item assignment

lat, lon = point            # 풀어서 받기
print(lat, lon)             # 37.5 127.0

x, y = 10, 20               # 괄호는 생략할 수 있다
x, y = y, x                 # 맞바꾸기
print(x, y)                 # 20 10
