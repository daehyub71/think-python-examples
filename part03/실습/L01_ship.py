total = 29999
if total >= 50000:
    fee = 0
elif total >= 30000:
    fee = 2000
else:
    fee = 3500
print(f"배송비 {fee}원")
