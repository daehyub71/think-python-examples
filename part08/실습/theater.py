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
        print(f"{count}장 예매 완료")
