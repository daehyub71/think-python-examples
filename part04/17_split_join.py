# 생각하는 파이썬 Part 4 · split 과 join
# (강의 슬라이드: 자른다 → 다듬는다 → 합친다)

raw = " 김산공 ,  품질팀 , 2024-03 "

parts = raw.split(",")                  # 자른다 — 쉼표에서 잘라 리스트로
print(parts)                            # [' 김산공 ', '  품질팀 ', ' 2024-03 ']

cells = [c.strip() for c in parts]      # 다듬는다 — 조각마다 strip()
print(cells)                            # ['김산공', '품질팀', '2024-03']

clean = ",".join(cells)                 # 합친다 — "이 쉼표로 꿰어라"
print(clean)                            # 김산공,품질팀,2024-03
