from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]

n = first([30, 10, 20])
s = first(["가", "나"])
reveal_type(n)
reveal_type(s)
