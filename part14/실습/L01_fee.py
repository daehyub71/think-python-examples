FEES = {"서울": 3000, "부산": 3500}

def fee_for(region):
    return FEES.get(region, 5000)       # 그 밖의 지역은 5000

def total_fee(orders):
    total = 0
    for region in orders:
        total += fee_for(region)
    return total

print(total_fee(["서울", "부산", "제주"]))
