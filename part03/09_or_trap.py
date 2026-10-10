# 생각하는 파이썬 Part 3 · or 의 함정과 is None
# (강의 슬라이드: or 기본값의 함정)

alarm = 0                   # 알림을 끄려고 0 을 골랐다
times = alarm or 3
print(times)                # 3 ← 0 이 거짓으로 치는 값이라 조용히 덮였다

# "없을 때만"이라고 정확히 묻는다
times = 3 if alarm is None else alarm
print(times)                # 0 ← 이제 0 이 살아남는다

alarm = None                # 아직 정하지 않음
print(3 if alarm is None else alarm)    # 3
