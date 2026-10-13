import logging

a = logging.getLogger("shop")
b = logging.getLogger("shop")    # 같은 이름으로 다시
print(a is b)
