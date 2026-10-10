# 생각하는 파이썬 Part 5 · 함수는 값이다


def to_km(m):
    return m / 1000

def to_mile(m):
    return round(m / 1609.344, 2)

print(to_km(4200))                  # 4.2 — 괄호 O: 실행
print(to_km)                        # <function to_km at 0x...> — 괄호 X: 함수라는 값

f = to_km                           # 이름표를 하나 더
print(f(4200))                      # 4.2

table = {"km": to_km, "mile": to_mile}      # 함수를 딕셔너리에 담는다
print(table["mile"](4200))          # 2.61
