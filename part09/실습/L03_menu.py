MENU = {"김밥": 4000, "라면": 4500}

def find_price(name: str) -> int | None:
    return MENU.get(name)

price = find_price("우동")
if price is None:
    print("우동은 메뉴에 없습니다")
else:
    print(price + 500)
