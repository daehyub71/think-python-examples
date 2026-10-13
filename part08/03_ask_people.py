def ask_people():
    while True:
        raw = input("몇 명인가요? ")
        try:
            return int(raw)
        except ValueError:
            print(f"'{raw}' 는 숫자가 아닙니다")

people = ask_people()
print(f"{people}명으로 나눕니다")
