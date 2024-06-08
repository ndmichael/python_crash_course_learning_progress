from pathlib import Path

path = Path('prim_athens.txt')

content = path.read_text(encoding='utf-8')
lines = content.splitlines()

counter = 0

for line in lines:
    if len(line) == 0:
        continue
    print(f"total words: {len(line)}, the appears: {line.lower().count('the ')}")
    counter += line.lower().count('the ')


print(f"\ncounter: {counter}")
print(f"total the is: {content.lower().count('the ')}")