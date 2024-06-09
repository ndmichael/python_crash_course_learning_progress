from name_func import get_formatted_name

while True:
    print("Enter q to quit.")
    first = input("Enter first name: ")
    if first.lower() == 'q':
        break
    last = input("Enter last name: ")
    if last.lower == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\t Your formatted name: {formatted_name} \n")