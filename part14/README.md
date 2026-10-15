# 생각하는 파이썬 Part 14 · 마무리 (디버깅 · 파이썬다운 코드와 도구 · 다음 단계) — 예제 소스

강의에 나온 코드를 그대로 실행해 볼 수 있게 파일로 모았습니다. ⚠️ 표시는 **일부러 오류가 나게** 만든 파일입니다.

- 실행: 이 폴더에서 `python3 파일이름.py`
- `ruff` 는 켠 가상환경(Part 13)에서 `pip install ruff` 로 설치합니다.

| 파일 | 내용 |
|---|---|
| `01_syntax.py` ⚠️ | 구문 오류 — 짚어 준 줄과 메시지 |
| `02_traceback.py` ⚠️ | 트레이스백을 마지막 줄부터 거꾸로 읽기 |
| `03_print_debug.py` | `f"{x=}"` 로 값 찍어 보기 — 3쪽이어야 하는데 2쪽 |
| `04_breakpoint.py` | `breakpoint()` 로 멈춰 세우기 (실행하면 `(Pdb)` 가 뜹니다 — `p name, weight` · `c` 를 쳐 보세요) |
| `05_mre.py` ⚠️ | 재현되는 가장 작은 예 — 이름 한 글자 오타 |
| `06_messy.py` | `ruff format 06_messy.py` 로 정리해 볼 지저분한 코드 |
| `07_lint.py` | `ruff check 07_lint.py` 로 검사해 볼 코드(F401 · F841 · F821) |
| `practice_tb.py` ⚠️ | 직접 해보기 ① — 트레이스백 세 줄 적기 |
| `practice_long.py` | 직접 해보기 ② — 오류 없이 이상한 영수증, MRE 로 줄이기 |
| `practice_answers.py` | ①~③ 풀이 |
| `실습/` | 영상의 실습 화면에서 실행한 파일(L01~L05, 고친 뒤의 모습) |
