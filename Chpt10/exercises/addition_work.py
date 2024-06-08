

while True:
    '''Code to kep looping and adding 2 numbers together'''
    print("Enter q to terminate: ")
    try:
        num1 = input("Enter first number: ")
        if num1.lower() == 'q' :
            break
        num2 = input("Enter second number: ")
        if num2.lower() == 'q':
            break
        result = int(num1) + int(num2)
    except ValueError:
        print("Inputs should be numbers friend!")
    else:
        print(f"{num1} + {num2} = {result} \n")


