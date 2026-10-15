import os

token = os.getenv("API_TOKEN")
every = os.getenv("CHECK_EVERY", "30")    # 없으면 기본값
print(token)
print(every, type(every))
print(int(every) * 2)                     # 숫자로 바꿔야 계산된다
