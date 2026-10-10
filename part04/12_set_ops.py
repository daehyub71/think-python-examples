# 생각하는 파이썬 Part 4 · 집합 연산
# (강의 슬라이드: 두 모음을 견주기)

last = {"C-01", "C-02", "C-03", "C-05"}     # 지난달 주문 고객
this = {"C-02", "C-03", "C-04"}             # 이번 달 주문 고객

print(sorted(last & this))  # ['C-02', 'C-03'] — 둘 다: 유지
print(sorted(last - this))  # ['C-01', 'C-05'] — 지난달에만: 이탈
print(sorted(this - last))  # ['C-04']         — 이번 달에만: 신규
print(sorted(last | this))  # 한 번이라도 주문한 전체
