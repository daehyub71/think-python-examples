import threading

def run_together(func, threads, times):
    """func(times) 를 스레드 threads 개로 동시에 돌리고, 모두 끝날 때까지 기다린다."""
    team = [threading.Thread(target=func, args=(times,)) for _ in range(threads)]
    for t in team:
        t.start()
    for t in team:
        t.join()
