from typing import Protocol

class Chargeable(Protocol):
    def charge(self, minutes: int) -> int: ...

class Phone:                      # 상속하지 않았다
    def charge(self, minutes: int) -> int:
        return minutes * 2

class Chair:
    pass

def plug_in(device: Chargeable) -> None:
    print(device.charge(30), "%")

plug_in(Phone())
plug_in(Chair())
