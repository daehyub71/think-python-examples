class Parcel:
    def __init__(self, weight):
        self.weight = weight
    def cost(self):
        return 3000 + self.weight * 500

class ColdParcel(Parcel):
    def cost(self):
        return super().cost() + 2000

class FragileParcel(Parcel):
    def cost(self):
        return super().cost() + 1500

parcels = [Parcel(4), ColdParcel(4), Parcel(1), FragileParcel(2)]
for p in parcels:
    print(type(p).__name__, p.cost())
print(sum(p.cost() for p in parcels))
