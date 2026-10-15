import cProfile

def top3(ranked):
    return ranked[:3]

def report(scores):
    ranked = sorted(scores, reverse=True)   # 한 번만
    for _ in range(300):
        top3(ranked)

scores = [(n * 37) % 1000 for n in range(5000)]
cProfile.run("report(scores)", sort="tottime")
