import os

os.environ["SEND_MAIL"] = "false"   # 환경 변수에 "false"
print(bool(os.getenv("SEND_MAIL")))
print(os.getenv("SEND_MAIL", "false").lower() == "true")
