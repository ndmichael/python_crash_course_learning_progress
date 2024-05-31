from pathlib import Path

path = Path('pi_millions.txt')

content = path.read_text()
lines = content.splitlines()[:5]

pi_string = ''

for line in lines:
    pi_string += line

print(pi_string)

