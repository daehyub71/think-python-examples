prices = [3000, 4500, 1200, 8000]
biggest = 0
for p in prices:
    if p > biggest:
        biggest = p
    print(p, biggest)
print("가장 비싼 값", biggest)
