# 생각하는 파이썬 Part 5 · 독스트링 — 함수에 붙이는 설명서


def box_fee(weight):
    """무게(kg)를 받아 택배 요금을 돌려준다."""
    return 3000 + weight * 500

print(box_fee.__doc__)              # 무게(kg)를 받아 택배 요금을 돌려준다.
help(box_fee)                       # 설명서 전체
