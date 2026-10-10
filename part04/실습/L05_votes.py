votes = ["짜장", "짬뽕", "짜장", "볶음밥", "짜장", "짬뽕"]
counts = {}
for v in votes:
    counts[v] = counts.get(v, 0) + 1
    print(counts)
