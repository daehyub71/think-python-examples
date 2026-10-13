def find_member(members: dict[int, str], number: int) -> str | None:
    return members.get(number)

name = find_member({1: "haneul"}, 2)
print(name.upper())
