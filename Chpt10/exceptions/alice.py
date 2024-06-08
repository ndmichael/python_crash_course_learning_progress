from pathlib import Path

path = Path("alice.txt")
try:
    content = path.read_text(encoding='utf-8')
    
except:
    print("File not found.")
else:
    lines = content.split()
    total_words  = len(lines)
    print(f"The file {path} has about {total_words} words")