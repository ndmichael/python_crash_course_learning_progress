prompt = "If you could visit one place in the world\n"
prompt += "Where would you go? "

flag = True

vacations = {}

while flag:
    vacation = input(prompt).lower()

    if vacation in vacations:
        vacations[vacation] += 1
    else:
        vacations[vacation] = 1

    choice = input("\ncontinue voting, yes or no? ")

    if choice.lower() in ['n', 'no']:
        flag = False


print("******* Pool results *******")
print("-" * 28)
print
for k, v in vacations.items():
    print(f"{k}: {v}")