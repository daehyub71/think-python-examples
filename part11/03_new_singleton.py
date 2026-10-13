class Settings:
    _only = None                 # 하나뿐인 객체 자리

    def __new__(cls):
        if cls._only is None:    # 처음 한 번만 만든다
            cls._only = super().__new__(cls)
            cls._only.theme = "light"
        return cls._only         # 그 뒤로는 그것을 준다

a = Settings()
b = Settings()
b.theme = "dark"
print(a.theme, a is b)
