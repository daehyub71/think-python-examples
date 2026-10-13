with open("walk.txt", "w", encoding="utf-8") as f:
    f.write("월 6200\n화 8450\n수 7300\n")

with open("walk.txt", encoding="utf-8") as f:
    text = f.read()
print(repr(text))

with open("walk.txt", encoding="utf-8") as f:
    lines = f.readlines()
print(lines)

with open("walk.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
