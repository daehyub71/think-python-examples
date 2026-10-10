class Parcel:
    def __init__(self, weight):
        self.weight = weight

    def cost(self):
        return 3000 + self.weight * 500

    def label(self):
        return f"{self.weight}kg · {self.cost():,}원"

class ColdParcel(Parcel):
    def cost(self):
        return super().cost() + 2000

class QuickParcel(Parcel):
    def __init__(self, weight, hours):
        super().__init__(weight)
        self.hours = hours

    def cost(self):
        return super().cost() * 2

print(QuickParcel(4, 3).label())
