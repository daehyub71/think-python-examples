import json

def load_log():
    try:
        with open("walklog.json", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def add(day, steps):
    log = load_log()
    log.append({"요일": day, "걸음": steps})
    with open("walklog.json", "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

add("월", 6200)
add("화", 8450)
print(load_log())
