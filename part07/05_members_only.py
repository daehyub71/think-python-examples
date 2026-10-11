# 생각하는 파이썬 Part 7 · 문지기 — 원래 함수를 실행할지 말지 정한다


session = {"name": "하늘", "member": False}

def members_only(func):
    def wrapper(*args, **kwargs):
        if not session["member"]:
            raise PermissionError("회원만 볼 수 있습니다")   # 여기서 막는다 — 원래 함수는 부르지도 않는다
        return func(*args, **kwargs)
    return wrapper

@members_only
def coupon():
    return f"{session['name']}님의 쿠폰 3장"

session["member"] = True
print(coupon())                      # 하늘님의 쿠폰 3장

session["member"] = False
print(coupon())                      # ⚠️ PermissionError: 회원만 볼 수 있습니다
