# 생각하는 파이썬 — 강의 예제 소스

유튜브 「백발개발자의 바이브코딩」의 강의 **바이브코딩 기초 : 생각하는 파이썬 [문법편]**에 나오는 예제 코드와 「직접 해보기」 풀이입니다.
로그인 없이 내려받아 그대로 실행해 볼 수 있습니다.

- 책(무료 전자책): https://wikidocs.net/book/20360
- 유튜브 채널: https://www.youtube.com/@50VibeLog

## 폴더

| 폴더 | 강의 | 영상 |
|---|---|---|
| [`part00`](part00) | Part 0 · 시작하기 전에 | [1편 생각하는 법](https://youtu.be/YI5_cP_p3u4) · [2편 설치와 첫 프로그램](https://youtu.be/LnZENdgPgbk) |
| [`part01`](part01) | Part 1 · 가장 작은 조각들 | [1편 프로그램이란](https://youtu.be/BnQqFFS82-Q) · [2편 값과 변수](https://youtu.be/M2F7C7naxqk) · [3편 연산자](https://youtu.be/o9vKj2JjzzQ) · [4편 입력과 출력](https://youtu.be/ZLsXRLfgPhk) |
| [`part02`](part02) | Part 2 · 파이썬은 어떻게 실행되는가 | [1편 소스 코드가 실행되기까지](https://youtu.be/44N33MgXsQI) · [2편 바이트코드와 가상 머신](https://youtu.be/IJ0QJKcewBA) · [3편 메모리 모델](https://youtu.be/-RkAMCOM7x4) |
| [`part03`](part03) | Part 3 · 흐름을 다루기 | [1편 조건문과 단락 평가](https://youtu.be/nwE4Ia6rLts) · [2편 반복문과 컴프리헨션](https://youtu.be/6_zO2-wUOa8) |
| [`part04`](part04) | Part 4 · 데이터를 담는 그릇 — 자료구조 | [1편 리스트 · 튜플 · 딕셔너리](https://youtu.be/5Km1Or9tXo4) · [2편 셋 · 문자열 · 고르는 법](https://youtu.be/YV5WUFENW6Y) |
| [`part05`](part05) | Part 5 · 함수와 함수형 프로그래밍 | 준비 중 |
| [`part06`](part06) | Part 6 · 객체로 세상을 모델링하기 — OOP | 준비 중 |
| [`part07`](part07) | Part 7 · 함수를 확장하기 — 데코레이터와 클로저 | 준비 중 |
| [`part08`](part08) | Part 8 · 견고한 프로그램 — 예외와 파일 입출력 | 준비 중 |
| [`part09`](part09) | Part 9 · 타입으로 안전하게 — 타입 힌트 · typing · mypy | 준비 중 |
| [`part10`](part10) | Part 10 · 동시에 여러 일 하기 — 스레드와 프로세스 | 준비 중 |
| [`part11`](part11) | Part 11 · 잘 설계된 코드 — 디자인 패턴 | 준비 중 |
| [`part12`](part12) | Part 12 · 측정하고 빠르게 — 성능 분석 | 준비 중 |
| [`part13`](part13) | Part 13 · 실무 프로젝트의 뼈대 — 가상환경 · .env · logging | 준비 중 |
| [`part14`](part14) | Part 14 · 마무리 — 디버깅 · 파이썬다운 코드와 도구 · 다음 단계 | 준비 중 |

각 폴더의 `README.md`에 파일별 설명이 있습니다.

- 번호가 붙은 파일(`01_…py`)은 강의 슬라이드의 예제입니다.
- `실습/` 폴더는 영상의 「실습」 화면에서 직접 실행해 보는 코드입니다. `.txt` 파일은 대화형 모드(`>>>`)에서 한 줄씩 쳐 보는 내용입니다.
- `practice_answers.py`는 「직접 해보기」 풀이입니다. 먼저 직접 풀어 본 다음에 열어 보세요. (Part 0의 풀이는 `02_repl_practice.py`, `05_error_paren.py`에 들어 있습니다.)
- ⚠️ 표시가 있는 파일은 **일부러 오류가 나게** 만든 것입니다. 오류 메시지의 마지막 줄부터 읽어 보세요.

## 실행 방법

파이썬 3.11 이상이 필요합니다. 이 저장소를 내려받은 뒤(초록색 `Code` 버튼 → `Download ZIP`), 해당 폴더에서 실행합니다.

```
python3 01_average.py        # macOS
python 01_average.py         # Windows (안 되면 py 01_average.py)
```

코드와 출력은 실제로 실행해 확인한 것입니다. 버전에 따라 오류 메시지의 문구는 조금 다를 수 있습니다.
