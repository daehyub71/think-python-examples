def box_fee(weight, base=3000):
    return base + weight * 500

print("__name__ =", __name__)

if __name__ == "__main__":
    print("시험:", box_fee(4))
