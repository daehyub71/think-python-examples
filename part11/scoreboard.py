# 직접 해보기 ① — 점수판 객체를 모듈에 하나 만들어 둔다

class _Scoreboard:
    def __init__(self):
        self.points = 0

    def add(self, n):
        self.points += n

board = _Scoreboard()            # 딱 한 번 만든다
