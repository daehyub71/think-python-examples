# 생각하는 파이썬 Part 6 · 캡슐화 — property 로 창구 만들기


class Battery:
    def __init__(self, level):
        self.level = level              # 아래의 쓰는 창구를 거친다

    @property
    def level(self):                    # 읽는 창구
        return self._level

    @level.setter
    def level(self, value):             # 쓰는 창구 — 확인하고 넣는다
        if not 0 <= value <= 100:
            raise ValueError("충전량은 0에서 100 사이여야 합니다")
        self._level = value

    @property
    def is_low(self):                   # 계산해서 주는, 읽기 전용 속성
        return self._level < 20

bt = Battery(80)
bt.level = 15                       # 변수처럼 쓰지만 안에서 검사가 돈다
print(bt.level, bt.is_low)          # 15 True
# bt.level = 150                    # 주석을 풀면 ValueError
# bt.is_low = True                  # 주석을 풀면 AttributeError — 쓰는 창구가 없다
# Battery(-5)                       # 주석을 풀면 ValueError — 만들 때도 같은 창구를 거친다
