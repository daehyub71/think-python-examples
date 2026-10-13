def read_number(text):
    try:
        return int(text)
    finally:
        print("finally: 돌려주기 직전에도 실행")

print(read_number("42"))
