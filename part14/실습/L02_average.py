scores = {"민수": 80, "지영": None, "현우": 90}

present = [s for s in scores.values() if s is not None]
average = sum(present) / len(present)
print(f"출석자 평균 {average:.1f}점")
