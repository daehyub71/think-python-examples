from notices import EmailNotice, SmsNotice

def make_notice(kind):
    if kind == "email":
        return EmailNotice()
    elif kind == "sms":
        return SmsNotice()
    raise ValueError(f"모르는 알림 종류: {kind}")

notice = make_notice("sms")
notice.send("주문이 접수되었습니다")
