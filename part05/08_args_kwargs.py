# 생각하는 파이썬 Part 5 · *args 와 **kwargs — 모으기와 풀기


def total(*prices):                 # 남는 위치 인자를 튜플로 모은다
    print(prices)
    return sum(prices)

print(total(1200, 800))             # (1200, 800) / 2000
print(total())                      # () / 0

def profile(name, **extra):         # 남는 키워드 인자를 딕셔너리로 모은다
    print(name, extra)

profile("이서준", team="물류", years=3)   # 이서준 {'team': '물류', 'years': 3}

# 호출할 때의 별표는 반대로 — 푼다
nums = [1200, 800, 500]
print(total(*nums))                 # (1200, 800, 500) / 2500

def order(menu, size="중", ice=True):
    return f"{menu} / {size} / {'얼음' if ice else '따뜻하게'}"

opts = {"size": "대", "ice": False}
print(order("라떼", **opts))        # 라떼 / 대 / 따뜻하게
