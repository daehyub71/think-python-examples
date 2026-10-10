# 생각하는 파이썬 Part 6 · 직접 해보기 풀이


from dataclasses import dataclass

# ① 사각형 클래스
class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(3, 4)
print(r.area(), r.perimeter())      # 12 14

# ② 할증이 붙는 입장권
class Ticket:
    def __init__(self, base):
        self.base = base

    def price(self):
        return self.base

class NightTicket(Ticket):
    def price(self):
        return super().price() + 2000       # 부모의 계산을 그대로 쓰고, 할증만 더한다

print(Ticket(12000).price())        # 12000
print(NightTicket(12000).price())   # 14000

# ③ 책 클래스 — __repr__ 과 __eq__
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.price})"

    def __eq__(self, other):
        return (self.title, self.author, self.price) == (other.title, other.author, other.price)

b1 = Book("파이썬", "홍길동", 25000)
b2 = Book("파이썬", "홍길동", 25000)
print(b1)                           # Book('파이썬', '홍길동', 25000)
print(b1 == b2, b1 is b2)           # True False — 내용은 같고, 물건은 둘

# ④ dataclass 로 다시
@dataclass(frozen=True)
class DBook:
    title: str
    author: str
    price: int

d1 = DBook("파이썬", "홍길동", 25000)
d2 = DBook("파이썬", "홍길동", 25000)
print(d1 == d2)                     # True
print(len({d1, d2}))                # 1 — 내용이 같으니 집합에는 한 권만 남는다
