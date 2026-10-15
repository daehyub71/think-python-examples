# 생각하는 파이썬 Part 14 · 직접 해보기 ② — MRE 로 줄이기
# 손님마다 장바구니를 만들어 영수증을 찍는 프로그램입니다. 오류는 나지 않지만 답이 이상합니다.
# 버그를 재현하는 가장 작은 코드를 다섯 줄 이내로 만들어 보세요.

PRICES = {"책": 15000, "펜": 1200, "공책": 3000, "가방": 42000}
MEMBERS = {"하늘"}


def add_item(item, cart=[]):
    cart.append(item)
    return cart


def subtotal(cart):
    return sum(PRICES[item] for item in cart)


def discount(name, amount):
    if name in MEMBERS:
        return amount * 95 // 100
    return amount


def receipt(name, items):
    cart = None
    for item in items:
        cart = add_item(item)
    amount = discount(name, subtotal(cart))
    print(f"{name}: {', '.join(cart)} — {amount:,}원")


receipt("하늘", ["책", "펜"])
receipt("바다", ["공책"])          # 공책 하나만 샀는데…
receipt("구름", ["가방", "펜"])
