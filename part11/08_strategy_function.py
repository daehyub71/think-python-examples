def no_discount(price):
    return price

def sale(price):
    return price * 90 // 100

def member(price):
    return price - 3000

def checkout(price, discount=no_discount):
    return discount(price)       # 계산 방법은 받아서 쓴다

print(checkout(20000))
print(checkout(20000, sale))
print(checkout(20000, member))
print(checkout(20000, lambda p: p // 2))
