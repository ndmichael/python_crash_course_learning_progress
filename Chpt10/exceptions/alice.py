from pathlib import Path

path = Path("alice.txt")

def count_word(path):
    """Code to words in a file"""
    try:
        content = path.read_text(encoding='utf-8')
        
    except:
        print("File not found.")
    else:
        lines = content.split()
        total_words  = len(lines)
        print(f"The file {path} has about {total_words} words")

count_word(path)