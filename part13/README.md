# 생각하는 파이썬 Part 13 · 실무 프로젝트의 뼈대 (가상환경 · .env · logging) — 예제 소스

강의에 나온 코드를 그대로 실행해 볼 수 있게 파일로 모았습니다.

- 먼저 이 폴더에 가상환경을 만들고 켠 다음 `python-dotenv` 를 깝니다(03·04 예제와 풀이에 필요).
  ```
  python3 -m venv .venv
  source .venv/bin/activate          # Windows: .venv\Scripts\activate
  pip install python-dotenv
  ```
- `.env` 의 `API_TOKEN=demo-7f3a9c` 는 강의용 **가짜 값**입니다. 실제 프로젝트에서는 `.env` 를 저장소에 올리지 않습니다(이 폴더에만 예제로 넣었습니다).
- 실행: 이 폴더에서 `python3 파일이름.py`

| 파일 | 내용 |
|---|---|
| `01_getenv.py` | `os.getenv` 와 기본값 — 값은 언제나 문자열 (`export API_TOKEN=demo-7f3a9c` 후 실행) |
| `02_bool_trap.py` | `bool("false")` 는 True — 글자로 묻는다 |
| `03_dotenv.py` | `.env` 를 `load_dotenv()` 로 읽기 |
| `04_config_main.py` | 설정을 `config.py` 한 곳에 모으고, 토큰은 가려서 찍기 |
| `05_levels.py` | 로그 레벨 다섯 단계 — 기본은 WARNING 부터 |
| `06_basic_config.py` | `basicConfig(level=...)` 로 문턱 바꾸기 |
| `07_handlers.py` | `getLogger` + 핸들러 두 개(화면 · 회전 파일) + Formatter |
| `08_exception.py` | `except` 안에서 `logger.exception` |
| `config.py` · `.env` · `.env.example` · `.gitignore` | 위 예제가 쓰는 파일과, 저장소용 틀 |
| `practice_answers.py` | 직접 해보기 풀이 |
| `실습/` | 영상의 실습 화면에서 실행한 파일(L01~L05) |
