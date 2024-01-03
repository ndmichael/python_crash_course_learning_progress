# testing my while loop skills

sandwich_orders = ["tuna", "mandarina", "marina", "chocolate"]
finished_sandwiches = []

flag = True

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