MENU = {"김밥": 4000, "라면": 4500}

def find_price(name: str) -> int | None:
    return MENU.get(name)

price = find_price("우동")
print(price + 500)
