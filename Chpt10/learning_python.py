from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
lines = content.splitlines()

pi_string = ''

for line in lines:
    line = line.replace('python', 'C')
    pi_string += line + '\n'


print(lines)
print(pi_string)