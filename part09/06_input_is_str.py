def total_price(price: int, count: int) -> int:
    return price * count

count = input("몇 개인가요? ")
print(total_price(4500, count))
