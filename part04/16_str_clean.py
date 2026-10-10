# 생각하는 파이썬 Part 4 · 문자열 다듬기
# (강의 슬라이드: 다듬기 — 세 가지면 대부분 된다)

print("  김산공  ".strip())                  # 김산공 — 양끝 공백을 벗긴다
print("Gmail.COM".lower())                  # gmail.com
print("010-1234-5678".replace("-", ""))     # 01012345678

print("품질팀" == "품질팀 ")                  # False — 공백 한 칸도 다른 글자다
