class EmailNotice:
    def send(self, text):
        print(f"[메일] {text}")

class SmsNotice:
    def send(self, text):
        print(f"[문자] {text}")
