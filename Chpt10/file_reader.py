from pathlib import Path

path = Path('pi_digits.txt')
lines = path.read_text().splitlines()

pi_string = ''

for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))
# print(f'current directory {Path.cwd()}')
