# Rental cars
msg = "What kindof car do you love to buy? "
car = input(msg)
print(f"Let me find you a {car} car.")

# Dining group 7.2
print("\n")
prompt = "How many people are in your dining group: "
num_of_people = int(input(prompt))

if num_of_people > 8:
    print("You will have to wait for an extra table.")
else:
    print("Table is ready")

# Multiples of 10,  7.3
print("\n")
number = int(input("Enter a number above 10: "))

if number % 10:
    print(f"{number} Not a multiple of 10")
else:
    print(f"{number} is a multiple of 10.")