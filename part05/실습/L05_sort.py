items = [
    {"name": "노트", "price": 2500, "stock": 40},
    {"name": "펜", "price": 1200, "stock": 120},
    {"name": "가방", "price": 38000, "stock": 7},
    {"name": "자", "price": 1200, "stock": 65},
]

for i in sorted(items, key=(lambda i: (-i["price"], i["name"]))):
    print(i["name"], i["price"], i["stock"])
