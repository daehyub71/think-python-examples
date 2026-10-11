# 생각하는 파이썬 Part 7 · 함수를 확장하기 (데코레이터와 클로저) — 예제 소스

강의에 나온 코드를 그대로 실행해 볼 수 있게 파일로 모았습니다.

- 실행: 이 폴더에서 `python3 파일이름.py` (Windows 는 `python 파일이름.py` 또는 `py 파일이름.py`)
- 결과는 코드 옆이나 아래 주석에 적어 두었습니다. 시간을 재는 예제는 컴퓨터마다 숫자가 다릅니다.
- ⚠️ 표시가 있는 파일은 **일부러 오류가 나게** 만든 것입니다. 오류 메시지의 마지막 줄을 읽어 보세요.

| 파일 | 내용 |
|---|---|
| `01_log_by_hand.py` | 함수를 받아 함수를 돌려준다 — 손으로 감싸기 |
| `02_at_syntax.py` | @ 는 "이름 = 데코레이터(이름)" 을 대신 적어 준다 |
| `03_skeleton.py` | 데코레이터의 뼈대 — 어떤 함수든 감쌀 수 있게 |
| `04_stopwatch.py` | 실행 시간을 재는 데코레이터 |
| `05_members_only.py` | ⚠️ 문지기 — 원래 함수를 실행할지 말지 정한다 |
| `06_stack_order.py` | 겹쳐 쓰기 — 함수에 가까운 것부터 감싼다 |
| `07_name_lost.py` | 감쌌더니 이름과 설명이 사라졌다 |
| `08_wraps.py` | functools.wraps — 이름과 설명을 겉으로 옮겨 준다 |
| `09_repeat.py` | 설정값을 받는 데코레이터 — 세 겹 |
| `10_repeat_unrolled.py` | @repeat(3) 을 손으로 풀어 쓰면 두 단계 |
| `11_cache.py` | 이미 만들어져 있는 데코레이터 — functools.cache |
| `12_retry.py` | 실패하면 다시 — retry |
| `13_already_used.py` | Part 6 에서 이미 쓴 데코레이터 — @property 와 @dataclass |
| `practice_answers.py` | 직접 해보기 풀이 |
