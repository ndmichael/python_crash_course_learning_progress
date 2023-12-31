person = {
    'first_name': 'tahir',
    'last_name': 'motashami',
    'age': 29,
    'city': 'stuttgart'
}

glossary = {
    "python": "Dynamic programming language",
    "list": "dynamic array use to store multiple items",
    "none": "absent of value"
}


for k,v in person.items():
    print(f"{k}: {v}")

print("\n")

print("Programming terms.")
for k,v in glossary.items():
    print(f"{k}: {v}")