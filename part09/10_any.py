from typing import Any

def shout(text: Any) -> str:
    return text.upper() + "!"

print(shout("coffee"))
print(shout(2026))
