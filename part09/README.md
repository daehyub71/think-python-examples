# 생각하는 파이썬 Part 9 · 타입으로 안전하게 (타입 힌트 · typing · mypy) — 예제 소스

강의에 나온 코드를 그대로 실행하고 검사해 볼 수 있게 파일로 모았습니다.

- 설치: `pip install mypy` (한 번만)
- 검사: 이 폴더에서 `mypy 파일이름.py` · 실행: `python3 파일이름.py` (Windows 는 `python` 또는 `py`)
- 이 폴더의 `pyproject.toml` 에는 강의 4부의 설정(힌트 없는 함수를 오류로 알림)이 들어 있습니다. 기본 설정으로 보려면 이 파일을 잠시 다른 이름으로 바꾸세요.
- ⚠️ 표시가 있는 파일은 **mypy 가 오류를 찾도록** 일부러 틀리게 만든 것입니다.

| 파일 | 내용 |
|---|---|
| `01_no_check.py` | ⚠️ 힌트는 강제가 아니다 — 실행은 되고, mypy 는 잡는다 |
| `02_function_hints.py` | 함수의 입구와 출구 · `-> None` · 기본값 |
| `03_collections.py` | `list[str]` · `dict[str, int]` · `tuple` · `set` |
| `04_optional.py` | ⚠️ 없을 수도 있는 값을 확인 없이 썼다 |
| `05_optional_checked.py` | `if price is None` 으로 먼저 확인 |
| `06_input_is_str.py` | ⚠️ `input()` 은 언제나 문자열 — [arg-type] |
| `07_return_mismatch.py` | ⚠️ 돌려주는 값이 약속과 다르다 — [return] · [return-value] |
| `08_none_dot.py` | ⚠️ None 일 수도 있는 값에 점을 찍었다 — [union-attr] |
| `09_union_literal.py` | ⚠️ `int | str` 과 `Literal` |
| `10_any.py` | `Any` — 검사는 통과하는데 실행하면 멈춘다 |
| `11_generic.py` | `TypeVar` 와 `reveal_type` (mypy 로만 봅니다 — 실행용이 아닙니다) |
| `12_protocol.py` | ⚠️ `Protocol` — 모양만 맞으면 통과 |
| `13_callable.py` | ⚠️ `Callable` — 함수의 모양 |
| `14_typeddict.py` | ⚠️ `TypedDict` — 딕셔너리의 모양 |
| `15_untyped.py` | 힌트 없는 함수 — 기본 설정에서는 통과, 이 폴더의 설정에서는 오류 |
| `practice_answers.py` | 직접 해보기 풀이 |
| `실습/` | 영상의 실습 화면에서 실행한 파일(L01~L08) |
