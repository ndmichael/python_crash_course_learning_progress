print("Give me 2 numbers and I will divide them.")
print("Enter 'q' to quit: ")

flag = True
msg = "program terminated."

while flag:
    first_num = input("Enter first number: ")
    if first_num.lower() == 'q':
        print(msg)
        break
    second_num = input("Enter second number: ")
    if second_num.lower() == 'q':
        print(msg)
        break
    try:
        result = int(first_num) / int(second_num)
    except:
        print("Cannot divide by zero.")
    else:
        print(f"result: {result}")
