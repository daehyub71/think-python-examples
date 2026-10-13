def reserve(count):
    if count < 1 or count > 4:
        raise ValueError(f"1~4장만 예매할 수 있습니다: {count}")
    return f"{count}장 예매 완료"

print(reserve(2))
try:
    print(reserve(7))
except ValueError as e:
    print("예매 실패 →", e)
