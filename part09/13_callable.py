from typing import Callable

def show_all(prices: list[int],
             rule: Callable[[int], str]) -> None:
    for p in prices:
        print(rule(p))

def label(price: int) -> str:
    return f"{price}원"

def half(price: int) -> int:
    return price // 2

show_all([3000, 4000], label)
show_all([3000, 4000], half)
