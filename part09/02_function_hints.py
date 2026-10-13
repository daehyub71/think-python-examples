def total_price(price: int, count: int = 1) -> int:
    return price * count

def show(name: str, price: int) -> None:
    print(f"{name}: {price:,}원")

show("김밥", total_price(4000, 2))
show("라면", total_price(4500))
