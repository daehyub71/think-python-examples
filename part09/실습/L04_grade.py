def grade(score: int) -> str:
    if score >= 60:
        return "합격"
    return "불합격"

print(grade(75))
print(grade(40))
