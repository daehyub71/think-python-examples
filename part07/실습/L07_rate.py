from retry_tool import retry

count = 0

@retry(times=2)
def fetch_rate():
    global count
    count += 1
    if count < 3:
        raise ConnectionError("응답 없음")
    return 1385.5

print(fetch_rate())
