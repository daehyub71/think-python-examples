import csv

rows = [["요일", "코스", "걸음"],
        ["월", "공원", 6200],
        ["화", "강변", 8450],
        ["수", "공원", 7300]]

with open("walks.csv", "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(rows)

with open("walks.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(row["코스"], row["걸음"])
