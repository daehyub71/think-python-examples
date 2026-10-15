def parse_weight(text):
    return float(text)

def total_weight(parcels):
    total = 0
    for name, weight in parcels:
        total += parse_weight(weight)
    return total

parcels = [("책", "1.2"), ("옷", "0.8"), ("그릇", "2.5kg")]
print(total_weight(parcels))
