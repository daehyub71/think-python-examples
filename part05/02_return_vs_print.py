# 생각하는 파이썬 Part 5 · return 은 돌려주고, print 는 보여 줄 뿐


def box_fee(weight):
    return 3000 + weight * 500      # 값을 돌려준다

def show_fee(weight):
    print(3000 + weight * 500)      # 화면에 찍기만 한다

fee = box_fee(4)
print(fee + 1000)                   # 6000 — 돌려받은 값은 계속 쓸 수 있다

fee = show_fee(4)                   # 화면에 5000
print(fee)                          # None — return 이 없으면 None 을 돌려준다

def grade(score):
    if score >= 60:
        return "합격"               # 여기서 함수가 끝난다
    return "불합격"

print(grade(72), grade(41))         # 합격 불합격
