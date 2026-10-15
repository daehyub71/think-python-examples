def total_weight(parcels):
    total = 0
    for name, weight in parcels:
        breakpoint()
        total += float(weight)
    return total

print(total_weight([("책", "1.2"), ("옷", "0.8")]))
