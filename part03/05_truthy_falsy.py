# 생각하는 파이썬 Part 3 · 참과 거짓
# (강의 슬라이드: 무엇이 "참"인가)

# 비었거나, 없거나, 0이면 거짓 — 나머지는 전부 참
items = []
if items:
    print(len(items), "개 있습니다")
else:
    print("목록이 비어 있습니다")         # 빈 리스트는 거짓

print(bool("0"))            # True — 글자 "0" 은 비어 있지 않은 문자열
print(bool(" "))            # True — 공백 한 칸도

# 직접 해보기 ② — 먼저 예상하고 실행하기 (repr() 는 따옴표까지 보여 준다)
for v in [0, "", "0", [], [0], None, " "]:
    print(repr(v), bool(v))
