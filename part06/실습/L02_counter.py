class Counter:
    def __init__(self):
        self.count = 0

    def up(self):
        self.count += 1

c = Counter()
c.up()
c.up()
print(c.count)
