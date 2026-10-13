class Settings:
    def __init__(self):
        self.theme = "light"

a = Settings()              # 화면 쪽에서 하나
b = Settings()              # 설정 창에서 또 하나
b.theme = "dark"            # 설정 창에서 바꿨다
print(a.theme, b.theme)
print(a is b)
