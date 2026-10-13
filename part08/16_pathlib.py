from pathlib import Path

folder = Path("records")
folder.mkdir(exist_ok=True)

path = folder / "walk.txt"
path.write_text("월 6200\n", encoding="utf-8")

print(path)
print(path.exists(), path.name, path.suffix)
print(path.read_text(encoding="utf-8").strip())
print(list(folder.glob("*.txt")))
