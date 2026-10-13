with open("walk.txt", "w", encoding="utf-8") as f:
    f.write("월 6200\n")
    f.write("화 8450\n")

with open("walk.txt", "a", encoding="utf-8") as f:
    f.write("수 7300\n")

with open("walk.txt", encoding="utf-8") as f:
    total = 0
    for line in f:
        day, steps = line.split()
        total += int(steps)

print("합계", total)
