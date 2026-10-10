# 생각하는 파이썬 Part 6 · 연산자도 메서드다 — __add__ · __eq__ · __lt__


class Duration:
    def __init__(self, minutes):
        self.minutes = minutes

    def __str__(self):
        return f"{self.minutes // 60}시간 {self.minutes % 60}분"

    def __repr__(self):
        return f"Duration({self.minutes})"

    def __add__(self, other):           # a + b
        return Duration(self.minutes + other.minutes)

    def __eq__(self, other):            # a == b
        return self.minutes == other.minutes

    def __lt__(self, other):            # a < b
        return self.minutes < other.minutes

a = Duration(50)
b = Duration(75)
print(a + b)                        # 2시간 5분
print(a == Duration(50))            # True
print(a < b)                        # True
print(max(a, b))                    # 1시간 15분
print(sorted([b, a]))               # [Duration(50), Duration(75)]
