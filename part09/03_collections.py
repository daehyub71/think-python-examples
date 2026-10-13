friends: list[str] = ["하늘", "바다"]
stock: dict[str, int] = {"연필": 30, "공책": 12}
spot: tuple[float, float] = (37.5, 127.0)
tags: set[str] = {"문구", "학용품"}

def average(scores: list[int]) -> float:
    return sum(scores) / len(scores)

print(average([80, 90, 100]))
