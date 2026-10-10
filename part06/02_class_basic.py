# 생각하는 파이썬 Part 6 · 클래스와 객체 · __init__ · self


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
b = StampCard("오민재")             # stamps 를 생략하면 0
print(a.name, a.stamps)             # 한지우 3
print(b.name, b.stamps)             # 오민재 0
print(type(a))                      # <class '__main__.StampCard'>
print(a is b)                       # False — 서로 다른 객체
