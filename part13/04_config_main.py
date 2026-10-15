import config

def mask(secret):
    return secret[:4] + "*" * (len(secret) - 4)

print(f"{config.BOT_NAME} — {config.CHECK_EVERY}분마다 확인")
print("메일 알림:", config.SEND_MAIL)
print("토큰:", mask(config.API_TOKEN))      # 원문은 찍지 않는다
