from pathlib import Path


def count_word(path):
    """Code to words in a file"""
    try:
        content = path.read_text(encoding='utf-8')
        
    except FileNotFoundError:
        print("File not found.")
    else:
        lines = content.split()
        total_words  = len(lines)
        print(f"The file {path} has about {total_words} words")


filenames = ['alice.txt', 'pi_digits.txt', 'mob.txt', 'pi_millions.txt']

for file in filenames:
    path = Path(file)
    count_word(path)