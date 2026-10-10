# 생각하는 파이썬 Part 6 · 클래스 변수와 인스턴스 변수 · 리스트 함정


class Visitor:
    total = 0                           # 클래스 변수 — 모두가 함께 쓰는 값 하나

    def __init__(self, name):
        self.name = name                # 인스턴스 변수 — 객체마다 따로
        Visitor.total += 1
        self.number = Visitor.total

v1 = Visitor("가")
v2 = Visitor("나")
print(v1.number, v2.number, Visitor.total)      # 1 2 2

class Team:
    members = []                        # ⚠️ 모든 객체가 같은 리스트를 쓴다

t1 = Team()
t2 = Team()
t1.members.append("지우")
print(t2.members)                   # ['지우'] — 다른 팀에도 보인다

class TeamOk:
    def __init__(self):
        self.members = []               # 객체마다 새 리스트

t1 = TeamOk()
t2 = TeamOk()
t1.members.append("지우")
print(t2.members)                   # []
