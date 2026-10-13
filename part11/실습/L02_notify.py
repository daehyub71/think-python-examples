from notices import EmailNotice, SmsNotice

class PushNotice:
    def send(self, text):
        print(f"[앱 알림] {text}")

NOTICES = {"email": EmailNotice, "sms": SmsNotice}
NOTICES["push"] = PushNotice

def make_notice(kind):
    if kind not in NOTICES:
        raise ValueError(f"모르는 알림 종류: {kind}")
    return NOTICES[kind]()

for kind in ["email", "sms", "push"]:
    make_notice(kind).send("배송이 시작되었습니다")
