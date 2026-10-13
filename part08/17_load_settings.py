import json

DEFAULT = {"목표": 8000}

def load_settings(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("설정 파일이 없어 기본값을 씁니다")
    except json.JSONDecodeError as e:
        print("설정 파일이 깨졌습니다:", e)
    return DEFAULT

print(load_settings("my_settings.json"))

with open("broken.json", "w", encoding="utf-8") as f:
    f.write('{"목표": 8000,')
print(load_settings("broken.json"))
