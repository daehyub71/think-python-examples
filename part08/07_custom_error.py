class SoldOutError(Exception):
    def __init__(self, left):
        super().__init__(f"{left}장만 남았습니다")
        self.left = left

class Show:
    def __init__(self, title, seats):
        self.title = title
        self.seats = seats

    def reserve(self, count):
        if count > self.seats:
            raise SoldOutError(self.seats)
        self.seats -= count

show = Show("가을 음악회", 3)
show.reserve(2)
try:
    show.reserve(2)
except SoldOutError as e:
    print("좌석 부족:", e)
    print("남은 좌석:", e.left)
