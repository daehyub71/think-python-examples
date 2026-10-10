# 생각하는 파이썬 Part 5 · 큰 파일을 한 줄씩 흘려보내기


from pathlib import Path

Path("sample.log").write_text("INFO 시작\nERROR 디스크 부족\nINFO 재시도\nERROR 연결 끊김\n", encoding="utf-8")

def read_lines(path):
    with open(path, encoding="utf-8") as f:
        for line in f:              # 파일은 한 줄씩 내주는 이터레이터
            yield line.rstrip("\n")

errors = sum(1 for line in read_lines("sample.log") if "ERROR" in line)
print(errors)                       # 2
Path("sample.log").unlink()         # 연습용 파일 지우기
