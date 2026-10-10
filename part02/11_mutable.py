# 생각하는 파이썬 Part 2 · 불변과 가변
# (강의 슬라이드: 불변과 가변)


# 불변 — 바꾸려 하면 새 객체가 만들어진다 (int, float, str, bool, tuple)
s = "입고"
before = id(s)
s += " 완료"
print(s, id(s) == before)       # 입고 완료 False — 다른 객체가 됐다

# 가변 — 제자리에서 바뀐다 (list, dict, set)
cart = ["펜", "자"]
before = id(cart)
cart.append("풀")                # append — 리스트 끝에 하나 붙이기
print(cart, id(cart) == before) # ['펜', '자', '풀'] True — 같은 객체, 내용만 늘었다
