from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
lines = content.splitlines()

pi_string = ''

for line in lines:
    pi_string += line + ' '

print(lines)
print(pi_string)