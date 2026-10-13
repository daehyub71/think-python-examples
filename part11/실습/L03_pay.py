def no_discount(price):
    return price

def sale(price):
    return price * 90 // 100

def first_order(price):
    return price - 5000

def checkout(price, discount=no_discount):
    return discount(price)

print(checkout(20000))
print(checkout(20000, sale))
print(checkout(20000, first_order))
