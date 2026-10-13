def average(scores):
    try:
        totl = sum(scores)
        return total / len(scores)
    except:
        return 0

print(average([80, 90, 100]))
