from typing import Protocol

class Chargeable(Protocol):
    def charge(self, minutes: int) -> int: ...

class Phone:
    def charge(self, minutes: int) -> int:
        return minutes * 2

class Scooter:
    def charge(self, minutes: int) -> int:
        return minutes // 3

def plug_in(device: Chargeable) -> None:
    print(device.charge(30))

plug_in(Phone())
plug_in(Scooter())

# 영상의 마지막 단계에서는 Scooter.charge 가 str 을 돌려주게 바꿔, 모양이 다르면 mypy 가 걸러 내는 것을 보였습니다.
