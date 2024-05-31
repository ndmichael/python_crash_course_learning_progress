from pathlib import Path

path = Path("guest_book.txt")

names = ""
flag = False

while not flag:
    name = input("Enter your name or exit to terminate: ") + "\n"
    if(name.lower().rstrip('\n') == 'exit'):
        flag = True
    else:
        names += name

path.write_text(names)
    

