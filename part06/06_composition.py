# 생각하는 파이썬 Part 6 · 물려받을까, 가질까 — 포함(has-a)


class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def full(self):
        return f"{self.city} {self.street}"

class Parcel:
    def __init__(self, weight, address):
        self.weight = weight
        self.address = address          # 택배는 주소를 "가진다"

    def label(self):
        return f"{self.weight}kg → {self.address.full()}"

p = Parcel(4, Address("춘천시", "호반로 12"))
print(p.label())                    # 4kg → 춘천시 호반로 12
