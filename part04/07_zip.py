# 생각하는 파이썬 Part 4 · zip
# (강의 슬라이드: zip())

days = ["월", "화", "수"]
guests = [42, 35, 58]

for day, n in zip(days, guests):    # 양쪽에서 하나씩 꺼내 짝(튜플)을 만든다
    print(f"{day}요일: {n}명")

print(dict(zip(days, guests)))      # {'월': 42, '화': 35, '수': 58}
