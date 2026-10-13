def shout(text: str) -> str:
    return text.upper() + "!"

print(shout("coffee"))
print(shout(str(2026)))

# 영상의 마지막 단계에서는 shout(2026) 을 그대로 두어 mypy 가 잡는 것을 보였습니다.
# Argument 1 to "shout" has incompatible type "int"; expected "str"
