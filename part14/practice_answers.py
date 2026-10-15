# 생각하는 파이썬 Part 14 · 직접 해보기 풀이 (①~③)
# 실행: python3 practice_answers.py      (④ 나만의 작은 프로젝트는 여러분 몫입니다)

# ① 트레이스백 세 줄 ----------------------------------------------------------
#   (a) 무엇이: TypeError: unsupported operand type(s) for +: 'int' and 'str' — 숫자와 문자열을 더했다
#   (b) 어디서: practice_tb.py 의 add_minutes 안, return total + minutes
#   (c) 어떻게: summarize 의 반복문이 둘째 구간의 "35"(따옴표가 붙은 문자열)를 넘겼다 — 원인은 데이터
#   그래서 고칠 곳은 터진 줄이 아니라 데이터를 받는 자리다. 들어올 때 숫자로 바꿔 둔다.
TRIPS = [("서울→수원", 45), ("수원→평택", "35"), ("평택→천안", 30)]


def summarize(trips):
    total = 0
    for name, minutes in trips:
        total += int(minutes)          # 받는 자리에서 숫자로
    return total / 60


print("①", f"총 {summarize(TRIPS):.1f}시간")      # 총 1.8시간

# ② MRE — 다섯 줄 -------------------------------------------------------------
def add_item(item, cart=[]):          # 기본값 리스트는 def 를 읽을 때 한 번만 만들어진다 (Part 5)
    cart.append(item)
    return cart
print("② 재현:", add_item("책"), add_item("펜"))     # ['책', '펜'] ['책', '펜'] — 같은 리스트 하나


# 고친 판: 기본값은 None, 리스트는 부를 때마다 새로
def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
print("   고친 뒤:", add_item_fixed("책"), add_item_fixed("펜"))   # ['책'] ['펜']
# practice_long.py 에서는 receipt 가 손님마다 새 장바구니를 만들어 넘기게 고치면 된다:
#     cart = []
#     for item in items:
#         add_item(item, cart)

# ③ 내 옛 코드에 ruff -----------------------------------------------------------
#   $ pip install ruff            (켠 가상환경에서, Part 13)
#   $ ruff format 내파일.py        모양을 정리한다 — 바뀐 곳을 git diff 로 보면 좋다
#   $ ruff check 내파일.py         냄새를 짚는다 — F401 안 쓴 import, F841 안 쓴 변수, F821 없는 이름
#   $ ruff check --fix 내파일.py   [*] 표시가 붙은 것은 자동으로 고친다
#   가장 많이 나온 규칙 번호를 적어 두면, 그것이 앞으로 챙길 습관이다.
