# 생각하는 파이썬 Part 4 · 실습 풀이
# (강의 슬라이드: 직접 해보기)

# ① 자르기
w = "자료구조"
print(w[:2], w[-2:], w[::-1])           # 자료 구조 조구료자  ([::-1] 은 뒤집기)

# ② 입고 누적 — 세기 패턴에서 더하는 양만 바꾼다
inbound = [("A-101", 50), ("A-102", 30), ("A-101", 20)]
stock = {}
for code, qty in inbound:
    stock[code] = stock.get(code, 0) + qty
print(stock)                            # {'A-101': 70, 'A-102': 30}

# ③ 두 모임 견주기
last_year = {"지우", "민수", "해인"}
this_year = {"민수", "해인", "서연"}
print(sorted(last_year & this_year))    # ['민수', '해인'] — 둘 다 온 사람
print(sorted(last_year - this_year))    # ['지우']         — 작년에만 온 사람

# ④ 전화번호 통일
phone = " 010-1234 5678 "
print(phone.strip().replace("-", "").replace(" ", ""))   # 01012345678
