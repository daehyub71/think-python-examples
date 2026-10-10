# 생각하는 파이썬 Part 6 · 메서드 — 데이터와 규칙을 한 묶음으로


class StampCard:
    def __init__(self, name, stamps=0):
        self.name = name                # 이 객체의 주인 이름
        self.stamps = stamps            # 이 객체의 도장 수

    def add(self, count):
        if count <= 0:
            print("도장은 한 개 이상 찍어야 합니다")
            return
        self.stamps += count

    def use(self, need):
        if need > self.stamps:
            print("도장이 모자랍니다")
            return False
        self.stamps -= need
        return True

a = StampCard("한지우", 3)
b = StampCard("오민재")

a.add(4)
print(a.stamps, b.stamps)           # 7 0 — a 에 찍어도 b 는 그대로
a.add(-1)                           # 도장은 한 개 이상 찍어야 합니다

StampCard.add(b, 2)                 # b.add(2) 와 같은 뜻 — self 자리에 b
print(b.stamps)                     # 2

print(a.use(5), a.stamps)           # True 2
print(b.use(5), b.stamps)           # 도장이 모자랍니다 / False 2
