import json

settings = {"목표": 8000,
            "코스": ["공원", "강변"],
            "알림": {"켜짐": True, "시각": "07:30"}}

with open("settings.json", "w", encoding="utf-8") as f:
    json.dump(settings, f, ensure_ascii=False, indent=2)

with open("settings.json", encoding="utf-8") as f:
    data = json.load(f)

print(data == settings)
print(data["알림"]["켜짐"], data["목표"] + 2000)
