import cProfile

def make_ids():
    return list(range(5_000))

def count_known(ids):
    found = 0
    for n in range(0, 10_000, 2):
        if n in ids:              # 리스트에서 찾는다
            found += 1
    return found

def total(ids):
    return sum(ids)

def main():
    ids = make_ids()
    count_known(ids)
    for _ in range(100):
        total(ids)

cProfile.run("main()", sort="tottime")
