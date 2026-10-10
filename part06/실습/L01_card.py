class StampCard:
    def __init__(self, name, stamps=0):
        self.name = name
        self.stamps = stamps

    def add(self, count):
        if count <= 0:
            print("도장은 한 개 이상 찍어야 합니다")
            return
        self.stamps += count

a = StampCard("한지우", 3)
a.add(4)
a.add(-1)
print(a.stamps)
a.stamps = -5
print(a.stamps)
