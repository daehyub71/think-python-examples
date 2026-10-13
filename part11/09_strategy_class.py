from typing import Protocol

class Discount(Protocol):
    def apply(self, price: int) -> int: ...

class PercentOff:
    def __init__(self, percent: int):
        self.percent = percent   # 전략이 설정값을 들고 있다

    def apply(self, price: int) -> int:
        return price * (100 - self.percent) // 100

def checkout(price: int, discount: Discount) -> int:
    return discount.apply(price)

print(checkout(20000, PercentOff(10)))
print(checkout(20000, PercentOff(30)))
