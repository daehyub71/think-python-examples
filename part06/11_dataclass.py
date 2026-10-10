# 생각하는 파이썬 Part 6 · @dataclass 와 옵션 세 가지


from dataclasses import dataclass, field

@dataclass
class Song:
    title: str
    artist: str
    seconds: int = 180

s1 = Song("봄길", "하늘", 215)
print(s1)                                   # Song(title='봄길', artist='하늘', seconds=215)
print(s1 == Song("봄길", "하늘", 215))       # True
print(Song("새벽", "하늘"))                  # Song(title='새벽', artist='하늘', seconds=180)

@dataclass(frozen=True)                     # 만든 뒤에는 못 바꾼다
class Seat:
    row: str
    number: int

print({Seat("C", 7), Seat("C", 7)})         # {Seat(row='C', number=7)} — 집합에 넣을 수 있다
# Seat("C", 7).number = 8                   # 주석을 풀면 FrozenInstanceError

@dataclass(order=True)                      # 적은 순서대로 견준다
class Score:
    points: int
    name: str

print(sorted([Score(70, "나"), Score(95, "가"), Score(70, "가")]))
# [Score(points=70, name='가'), Score(points=70, name='나'), Score(points=95, name='가')]

@dataclass
class Playlist:
    name: str
    songs: list = field(default_factory=list)   # 객체마다 새 리스트

a = Playlist("출근")
b = Playlist("운동")
a.songs.append(s1)
print(len(a.songs), len(b.songs))           # 1 0
