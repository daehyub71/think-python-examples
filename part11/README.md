# 생각하는 파이썬 Part 11 · 잘 설계된 코드 (디자인 패턴 — 싱글톤 · 팩토리 · 전략) — 예제 소스

강의에 나온 코드를 그대로 실행해 볼 수 있게 파일로 모았습니다.

- 실행: 이 폴더에서 `python3 파일이름.py` (Windows 는 `python 파일이름.py` 또는 `py 파일이름.py`)
- 번호가 없는 파일은 다른 예제가 불러다 쓰는 파일입니다. 같은 폴더에 두세요.

| 파일 | 내용 |
|---|---|
| `01_two_settings.py` | 설정 객체가 둘이면 서로 어긋난다 |
| `02_module_singleton.py` | 모듈에 만들어 둔 객체를 함께 쓴다 (`appsettings.py` · `screen.py`) |
| `03_new_singleton.py` | `__new__` 로 클래스가 스스로 하나만 만들게 |
| `04_getlogger.py` | `logging.getLogger` 는 같은 이름에 같은 객체를 준다 |
| `05_factory_if.py` | 팩토리 — 종류에 따라 만들어 주는 함수 (`notices.py`) |
| `06_factory_dict.py` | 딕셔너리에서 클래스를 꺼내 만드는 팩토리 |
| `07_strategy_if.py` | 계산 방법이 함수 안에 박혀 있는 모습 |
| `08_strategy_function.py` | 전략 — 계산하는 함수를 넘긴다 |
| `09_strategy_class.py` | 설정값을 가진 전략 — 클래스와 Protocol |
| `appsettings.py` · `screen.py` · `notices.py` | 위 예제들이 불러다 쓰는 파일 |
| `practice_answers.py` | 직접 해보기 풀이 (`scoreboard.py` · `red_team.py` · `blue_team.py` 를 씁니다) |
| `실습/` | 영상의 실습 화면에서 실행한 파일(L01~L05) |
