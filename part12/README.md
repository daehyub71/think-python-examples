# 생각하는 파이썬 Part 12 · 측정하고 빠르게 (성능 분석 — timeit · cProfile · 메모리 재기) — 예제 소스

강의에 나온 코드를 그대로 실행해 볼 수 있게 파일로 모았습니다.

- 실행: 이 폴더에서 `python3 파일이름.py` (Windows 는 `python 파일이름.py` 또는 `py 파일이름.py`)
- 시간 값은 컴퓨터와 실행할 때마다 달라집니다. 영상과 숫자가 달라도 정상입니다. "어느 쪽이 몇 배쯤"을 보세요.
- 메모리 값(바이트 · MB)은 파이썬 버전에 따라 조금 다를 수 있습니다(영상은 Python 3.13).

| 파일 | 내용 |
|---|---|
| `01_one_shot.py` | 시계로 한 번씩 재면 잴 때마다 다르다 |
| `02_timeit_call.py` | `timeit.timeit` 은 전체 시간 · `repeat` 의 가장 빠른 기록 |
| `03_join_vs_plus.py` | 반복 `+=` 와 `join` 을 재서 견준다 |
| `04_cprofile.py` | `cProfile` 로 시간을 잡아먹는 함수 찾기 |
| `05_list_to_set.py` | 찾은 범인을 고치고 다시 잰다 — 리스트 대신 셋 |
| `06_getsizeof.py` | `sys.getsizeof` — 값 하나의 크기, 리스트는 겉 상자만 |
| `07_peak.py` | `tracemalloc` 의 지금 사용량과 최고치 |
| `08_list_vs_gen.py` | 리스트와 제너레이터의 최고 메모리 |
| `09_lru_cache.py` | `lru_cache` — 답을 기억해 두면 빨라지고, 메모리를 쓴다 |
| `practice_answers.py` | 직접 해보기 풀이 |
| `실습/` | 영상의 실습 화면에서 실행한 파일(L01~L05) |

명령줄에서 재 보기(영상 1부):

```
python3 -m timeit "sorted(range(500, 0, -1))"
python3 -m timeit -s "nums = list(range(500, 0, -1))" "sorted(nums)"
```
