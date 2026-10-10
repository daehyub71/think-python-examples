menu = {"김밥": 3500, "라면": 4500}
menu["돈가스"] = 9000
menu["라면"] = 5000
print(menu["라면"])
print(menu.get("우동", "없는 메뉴"))
for name, price in menu.items():
    print(name, price)
print(menu["우동"])
