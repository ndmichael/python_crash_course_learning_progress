from pathlib import Path

path = Path('programming.txt')
content = "I lov programming. \n"
content += "I love fighting. \n"
content += "I love building websites. \n"

path.write_text(content)
