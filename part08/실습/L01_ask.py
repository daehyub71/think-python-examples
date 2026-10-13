def ask_people():
    while True:
        raw = input("몇 명인가요? ")
        try:
            people = int(raw)
        except ValueError:
            print(f"'{raw}' 는 숫자가 아닙니다")
            continue
        if people < 1:
            print("한 명 이상이어야 합니다")
            continue
        return people

people = ask_people()
print(f"{people}명으로 나눕니다")
