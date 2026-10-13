import csv

totals = {}
with open("walks.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        course = row["코스"]
        steps = int(row["걸음"])
        totals[course] = totals.get(course, 0) + steps

print(totals)
