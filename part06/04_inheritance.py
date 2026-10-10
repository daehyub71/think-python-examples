# 생각하는 파이썬 Part 6 · 상속 · super() · 오버라이딩


class Parcel:
    def __init__(self, weight):
        self.weight = weight

    def cost(self):
        return 3000 + self.weight * 500

    def label(self):
        return f"{self.weight}kg · {self.cost():,}원"

class ColdParcel(Parcel):               # 괄호 안에 부모
    def cost(self):
        return super().cost() + 2000    # 부모의 계산에 2,000원 더하기

class QuickParcel(Parcel):
    def __init__(self, weight, hours):
        super().__init__(weight)        # 부모의 준비 먼저
        self.hours = hours              # 내 것 추가

    def cost(self):
        return super().cost() * 2

print(Parcel(4).cost())             # 5000
print(ColdParcel(4).cost())         # 7000
print(QuickParcel(4, 3).cost())     # 10000
print(ColdParcel(4).label())        # 4kg · 7,000원 — label 은 물려받고, cost 는 자기 것
print(isinstance(ColdParcel(4), Parcel))    # True — 냉장 택배는 택배다
