from dataclasses import dataclass

@dataclass(frozen=True)
class Track:
    seconds: int
    title: str

a = Track(215, "봄길")
a.seconds = 100
