# 생각하는 파이썬 Part 6 · __dict__ 와 __slots__


import tracemalloc

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class SlimColor:
    __slots__ = ("r", "g", "b")         # 속성의 자리를 미리 정한다

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

def memory_of(cls, n=100_000):
    tracemalloc.start()
    objs = [cls(255, 128, 0) for _ in range(n)]
    used, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return used

print(f"{memory_of(Color):,}")      # 약 10,400,000 바이트
print(f"{memory_of(SlimColor):,}")  # 약 6,400,000 바이트

c = Color(255, 128, 0)
print(c.__dict__)                   # {'r': 255, 'g': 128, 'b': 0}
c.alpha = 0.5                       # 없던 속성도 붙는다
print(c.__dict__)                   # {'r': 255, 'g': 128, 'b': 0, 'alpha': 0.5}

s = SlimColor(255, 128, 0)
# s.alpha = 0.5                     # 주석을 풀면 AttributeError
print(hasattr(s, "__dict__"))       # False
