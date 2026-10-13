def average(scores):
    try:
        total = sum(scores)
        return total / len(scores)
    except ZeroDivisionError:
        return 0

print(average([80, 90, 100]))
print(average([]))
