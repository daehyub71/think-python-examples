def clean(prices):
    return [p for p in prices if p > 0]

def add_tax(prices):
    return [p * 11 // 10 for p in prices]

def discount(prices):              # 10% 할인
    return [p * 9 // 10 for p in prices]

prices = [1000, -1, 2000]
step = add_tax(clean(prices))
step = discount(step)
print("합계", sum(step))
