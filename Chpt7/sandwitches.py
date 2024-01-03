# testing my while loop skills

sandwich_orders = ["tuna","pastrami", "mandarina","pastrami",  "marina", "pastrami", "chocolate"]
finished_sandwiches = []

flag = True
print("\nNo pastrami\n\n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    
while flag:
    sandwich = sandwich_orders.pop()
    print(f"I made youn a {sandwich.title()} sandwich.")
    finished_sandwiches.append(sandwich)

    if sandwich_orders == []:
        flag = False

print("\nSabdwiches made today")
print("-" * 22, end="\n\n")
for f_sandwiches in finished_sandwiches:
    print(f"{f_sandwiches}")