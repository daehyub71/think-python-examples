names = ["책", "옷", "그릇"]
weights = [1.2, 0.8, 2.5]
is_express = True

for no, (name, weight) in enumerate(zip(names, weights), start=1):
    if is_express:
        print(no, name, weight * 2)
