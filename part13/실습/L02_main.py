import os
import config

print(config.BOT_NAME, config.CHECK_EVERY, config.SEND_MAIL)
print(os.getenv("MAIL_HOST"))

# 영상의 둘째 단계: 마지막 줄을 print(os.environ["MAIL_HOST"]) 로 바꾸면 KeyError 로 바로 멈춘다
