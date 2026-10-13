from notices import EmailNotice, SmsNotice

NOTICES = {"email": EmailNotice, "sms": SmsNotice}

def make_notice(kind):
    if kind not in NOTICES:
        raise ValueError(f"모르는 알림 종류: {kind}")
    return NOTICES[kind]()       # 클래스를 꺼내서, 괄호로 만든다

for kind in ["email", "sms"]:
    make_notice(kind).send("배송이 시작되었습니다")
