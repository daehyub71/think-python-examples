prices = {"아메리카노": 3000, "라떼": 3800}

try:
    print(prices["모카"])
except KeyError:
    print("메뉴에 없습니다")
