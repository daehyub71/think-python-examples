def split_bill(total_text, people_text):
    try:
        total = int(total_text)
        people = int(people_text)
        return total / people
    except ValueError as e:
        print("숫자로 적어 주세요:", e)
    except ZeroDivisionError:
        print("인원은 한 명 이상이어야 합니다")

print(split_bill("45000", "3"))
split_bill("45000", "세명")
split_bill("45000", "0")
