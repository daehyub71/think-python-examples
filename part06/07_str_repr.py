# 생각하는 파이썬 Part 6 · __str__ 과 __repr__


class Duration:
    def __init__(self, minutes):
        self.minutes = minutes

    def __str__(self):                  # 사람이 읽을 모습
        return f"{self.minutes // 60}시간 {self.minutes % 60}분"

    def __repr__(self):                 # 개발자가 볼 모습
        return f"Duration({self.minutes})"

d = Duration(75)
print(d)                            # 1시간 15분
print([d])                          # [Duration(75)] — 리스트 안에서는 __repr__
print(repr(d))                      # Duration(75)
