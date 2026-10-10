class Distance:
    def __init__(self, km):
        self.km = km

    def __repr__(self):
        return f"Distance({self.km})"

    def __add__(self, other):
        return Distance(self.km + other.km)

    def __lt__(self, other):
        return self.km < other.km

walk = Distance(3.2)
run = Distance(5.0)
print(walk + run)
print(sorted([run, walk]))
