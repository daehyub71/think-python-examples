# 생각하는 파이썬 Part 1 · 이름 규칙
# (강의 슬라이드: 이름 짓는 규칙)


unit_price = 3500           # 좋음 — 소문자 단어를 밑줄로 잇는다
unitPrice = 3500            # 되기는 하지만 파이썬답지 않음
x = 3500                    # 무슨 값인지 알 수 없음

stock = 5
Stock = 9                   # 대문자와 소문자는 다른 글자 — stock 과 Stock 은 다른 이름
print(stock, Stock)         # 5 9

재고 = 10                    # 한글 이름도 되지만, 관례는 영문
print(재고)

# 아래 두 줄은 주석을 풀면 SyntaxError 가 납니다.
# 2nd = 10                  # 숫자로 시작할 수 없다 (invalid decimal literal)
# class = "생산2팀"          # 키워드는 이름으로 쓸 수 없다 (invalid syntax)
