# 생각하는 파이썬 Part 8 · 견고한 프로그램 (예외와 파일 입출력) — 예제 소스

강의에 나온 코드를 그대로 실행해 볼 수 있게 파일로 모았습니다.

- 실행: 이 폴더에서 `python3 파일이름.py` (Windows 는 `python 파일이름.py` 또는 `py 파일이름.py`)
- 11번부터는 실행하면 같은 폴더에 `walk.txt` · `walks.csv` · `settings.json` 같은 파일이 생깁니다. 지워도 됩니다.
- ⚠️ 표시가 있는 파일은 **일부러 오류가 나게** 만든 것입니다. 오류 메시지의 마지막 줄을 읽어 보세요.

| 파일 | 내용 |
|---|---|
| `01_traceback.py` | ⚠️ 예외가 나면 그 자리에서 멈춘다 — 트레이스백 읽기 |
| `02_try_except.py` | try / except — 받아내고 계속 간다 |
| `03_ask_people.py` | 입력을 숫자로 안전하게 받기(될 때까지 다시 묻기) |
| `04_many_except.py` | 사고 종류마다 다르게 받기 · as e |
| `05_else_finally.py` | else 와 finally — 네 칸이 실행되는 순서 |
| `06_raise.py` | raise — 잘못된 값은 입구에서 막는다 |
| `07_custom_error.py` | 내 예외 만들기 — SoldOutError |
| `08_lbyl.py` | 먼저 확인하고 꺼내기 |
| `09_eafp.py` | 일단 꺼내 보고, 안 되면 대응하기 |
| `10_catch_all.py` | 전부 잡기의 위험 — 오타까지 삼킨다 |
| `11_write.py` | open · write · close |
| `12_with.py` | with — 저절로 닫힌다 · "a" 로 덧붙이기 |
| `13_read.py` | 읽는 방법 세 가지 |
| `14_csv.py` | csv 로 표를 쓰고 읽기 |
| `15_json.py` | json 으로 딕셔너리를 저장하고 되살리기 |
| `16_pathlib.py` | pathlib — 경로를 / 로 조립하기 |
| `17_load_settings.py` | 파일과 예외 — 없거나 깨진 파일에 대비하기 |
| `practice_answers.py` | 직접 해보기 풀이 |
| `실습/` | 영상의 실습 화면에서 실행한 파일(L01~L08) |
