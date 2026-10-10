class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

red = Team("빨강")
blue = Team("파랑")
red.members.append("지우")
print(red.members)
print(blue.members)
