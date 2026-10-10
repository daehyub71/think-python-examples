# 생각하는 파이썬 Part 6 · 다형성 — 같은 명령, 객체마다 다른 행동


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

parcels = [Parcel(4), ColdParcel(4), QuickParcel(2, 3)]

for p in parcels:
    print(type(p).__name__, p.cost())       # Parcel 5000 / ColdParcel 7000 / QuickParcel 8000

print(sum(p.cost() for p in parcels))       # 20000 — 종류를 묻지 않는다
