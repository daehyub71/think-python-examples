raw = "  Kim, LEE ,park  "
names = raw.split(",")
print(names)
clean = [n.strip().lower() for n in names]
print(clean)
print(" / ".join(clean))
