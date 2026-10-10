class Battery:
    def __init__(self, level):
        self.level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if not 0 <= value <= 100:
            raise ValueError("충전량은 0에서 100 사이여야 합니다")
        self._level = value

bt = Battery(150)
