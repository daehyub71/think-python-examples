with open("walk.txt", "w", encoding="utf-8") as f:
    f.write("월 6200\n")
    f.write("화 8450\n")

with open("walk.txt", "a", encoding="utf-8") as f:
    f.write("수 7300\n")

print(f.closed)
