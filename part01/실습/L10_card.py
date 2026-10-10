name = "노트북"
price = 1290000
rate = 0.15
print(f"{name} 가격은 {price:,}원")
print(f"할인율 {rate:.0%}")
print(f"할인가 {price * (1 - rate):,.0f}원")
