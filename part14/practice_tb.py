# 생각하는 파이썬 Part 14 · 직접 해보기 ① — 트레이스백 세 줄 적기
# 실행하면 오류가 납니다. 고치기 전에 세 가지를 적어 보세요.
#   (a) 무엇이 잘못됐나     — 마지막 줄의 예외 이름과 메시지
#   (b) 어디서 터졌나       — 내 파일이 나오는 가장 아래 줄
#   (c) 그 값은 어떻게 왔나 — 위의 토막들, 그리고 데이터
# 힌트: 터진 줄을 고치는 것이 답이 아닐 수도 있습니다.

TRIPS = [("서울→수원", 45), ("수원→평택", "35"), ("평택→천안", 30)]   # 배송 구간별 걸린 분


def add_minutes(total, minutes):
    return total + minutes


def summarize(trips):
    total = 0
    for name, minutes in trips:
        total = add_minutes(total, minutes)
    return total / 60


print(f"총 {summarize(TRIPS):.1f}시간")
