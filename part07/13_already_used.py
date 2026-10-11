# 생각하는 파이썬 Part 7 · Part 6 에서 이미 쓴 데코레이터 — @property 와 @dataclass


from dataclasses import dataclass

@dataclass                           # 클래스를 받아 __init__ · __repr__ · __eq__ 를 붙여 돌려준다
class Seat:
    row: str
    number: int

class Battery:
    def __init__(self, level):
        self._level = level

    @property                        # 메서드를 받아 "괄호 없이 읽는 값"으로 바꿔 돌려준다
    def is_low(self):
        return self._level < 20

print(Seat("C", 12))                 # Seat(row='C', number=12)
print(Battery(15).is_low)            # True
