from typing import Literal

def cup_price(size: Literal["S", "M", "L"]) -> int:
    prices = {"S": 3000, "M": 3500, "L": 4000}
    return prices[size]

print(cup_price("M"))
print(cup_price("L"))
