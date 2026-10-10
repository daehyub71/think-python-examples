# 생각하는 파이썬 Part 2 · 버전 차이
# (강의 슬라이드: 명령 이름은 버전마다 다르다)


import dis
import sys

def area(w, h):
    return w * h

print("지금 파이썬:", sys.version.split()[0])
dis.dis(area)
# 3.11: LOAD_FAST w / LOAD_FAST h 두 줄
# 3.13: LOAD_FAST_LOAD_FAST (w, h) 한 줄
# 이름을 외우지 말고 "스택으로 한 명령씩"이라는 구조만 가져가세요.
