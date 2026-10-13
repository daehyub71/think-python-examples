def per_person(total, people):
    try:
        return total / people
    except ZeroDivisionError:
        print("인원이 0명이라 나눌 수 없습니다")
        return None

print(per_person(45000, 3))
print(per_person(45000, 0))
print("정산 끝")
