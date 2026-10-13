from typing import Protocol

class Chargeable(Protocol):
    def charge(self, minutes: int) -> int: ...

class Phone:
    def charge(self, minutes: int) -> int:
        return minutes * 2

class Scooter:
    def charge(self, minutes: int) -> str:
        return "충전 중"

def plug_in(device: Chargeable) -> None:
    print(device.charge(30))

plug_in(Phone())
plug_in(Scooter())
