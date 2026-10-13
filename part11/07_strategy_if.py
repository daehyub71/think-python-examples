def checkout(price, kind):
    if kind == "none":
        return price
    elif kind == "sale":
        return price * 90 // 100
    elif kind == "member":
        return price - 3000

print(checkout(20000, "sale"))
