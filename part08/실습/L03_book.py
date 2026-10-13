from theater import Show, SoldOutError

show = Show("가을 음악회", 3)
show.reserve(2)
try:
    show.reserve(2)
except SoldOutError as e:
    print("좌석 부족:", e)
    show.reserve(e.left)
