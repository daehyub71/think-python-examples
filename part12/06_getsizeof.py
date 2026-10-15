import sys

print(sys.getsizeof(7))
print(sys.getsizeof(10 ** 30))
print(sys.getsizeof("가"), sys.getsizeof("가" * 5000))

a, b, c = "가", "나", "다"
light = [a, b, c]
heavy = [a * 5000, b * 5000, c * 5000]
print(sys.getsizeof(light), sys.getsizeof(heavy))
