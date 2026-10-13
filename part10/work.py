def crunch(n):                   # 계산만 하는 일
    total = 0
    for i in range(n):
        total += i * i % 7
    return total
