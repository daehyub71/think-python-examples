from typing import Literal

def to_won(amount: int | str) -> str:
    return f"{int(amount):,}원"

def cup_price(size: Literal["S", "M", "L"]) -> int:
    return {"S": 3000, "M": 3500, "L": 4000}[size]

print(to_won(4500), to_won("4500"))
print(cup_price("M"))
print(cup_price("XL"))
print(to_won(4.5))
