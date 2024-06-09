import json
from pathlib import Path


path = Path("fav_number.json")

if path.exists():
    content = path.read_text()
    fav_number = json.loads()
    print(fav_number)
else:
    fav_number = input("Enter favourite number: ")
    content = json.dumps(fav_number)
    path.write_text(content)

    