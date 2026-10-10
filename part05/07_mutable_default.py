# 생각하는 파이썬 Part 5 · 가장 유명한 함정 — 기본값에 빈 리스트


def add_item(item, box=[]):         # ⚠️ 기본값 리스트는 def 를 읽을 때 한 번만 만들어진다
    box.append(item)
    return box

print(add_item("펜"))               # ['펜']
print(add_item("자"))               # ['펜', '자']  ← 쌓인다
print(add_item.__defaults__)        # (['펜', '자'],)

def add_item_ok(item, box=None):    # 기본값은 None, 리스트는 함수 안에서 만든다
    if box is None:
        box = []
    box.append(item)
    return box

print(add_item_ok("펜"))            # ['펜']
print(add_item_ok("자"))            # ['자']
