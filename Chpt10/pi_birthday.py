from pathlib import Path

path = Path('pi_millions.txt')
content = path.read_text()

lines = content.splitlines()
pi_strings = ''

for line in lines:
    pi_strings += line

birthday = input('Enter your birthday in the form of ddmmyy: ')
if birthday in pi_strings:
    print(f"Your birthday {birthday} appears in the first million digit of pi!")
else:
    print(f"You birthday doesn't appear in the first million digit of pi!")