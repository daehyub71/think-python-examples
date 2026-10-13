def summary(scores: list[int]) -> str:
    return f"평균 {sum(scores) / len(scores)}"

print(summary([80, 90]))
