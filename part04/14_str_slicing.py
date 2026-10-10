# 생각하는 파이썬 Part 4 · 문자열 슬라이싱
# (강의 슬라이드: 문자열도 줄 세운 묶음)

fname = "report_2024.xlsx"
print(fname[:6])            # report
print(fname[-5:])           # .xlsx        — 뒤에서 다섯 글자부터 끝까지
print(fname[:-5])           # report_2024  — 처음부터, 뒤 다섯 글자 앞까지

card = "1234567812345678"
print(card[-4:])            # 5678
