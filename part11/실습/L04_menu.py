menu = [("라면", 4500), ("김밥", 5000), ("돈가스", 9000)]

def by_name(item):
    return item[0]

def by_price(item):
    return item[1]

print(sorted(menu, key=by_name))
print(sorted(menu, key=by_price))
