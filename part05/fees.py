# 생각하는 파이썬 Part 5 · 내 모듈 — 다른 파일에서 import 해서 쓴다


def box_fee(weight, base=3000):
    """무게(kg)를 받아 택배 요금을 돌려준다."""
    return base + weight * 500

BASE = 3000

if __name__ == "__main__":          # 이 파일을 직접 실행했을 때만
    print("시험:", box_fee(4))      # 시험: 5000
