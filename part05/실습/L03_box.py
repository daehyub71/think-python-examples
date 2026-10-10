def add_item(item, box=None):
    if box is None:
        box = []
    box.append(item)
    return box

print(add_item("펜"))
print(add_item("자"))
print(add_item.__defaults__)
