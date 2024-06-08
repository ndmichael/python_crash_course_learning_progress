from pathlib import Path

files = ['cat.txt', 'jagaban.txt', 'dog.txt']

def read_path(path):
    try:
        content = path.read_text(encoding="utf-8")
        words = content.split()
    except FileNotFoundError:
        print("File doesn't exist!")
    else:
        print(f"in {path} contains {len(words)} words.")
    finally:
        print("memory cleaned. \n")

for file in files:
    path = Path(file)
    read_path(path)
