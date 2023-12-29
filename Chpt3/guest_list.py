guests = ['tahir', 'daniela', 'jamal']
msg = "You are invited for my dinner party."

print(f"{guests[0].title()}, {msg}")
print(f"{guests[1].title()}, {msg}")
print(f"{guests[-1].title()}, {msg}")

print("\n\nI have found a new table.")
guests.insert(0, 'rose')
guests.insert(2, 'toba')
guests.append("Juisy")

print(guests)

# 3.7. shrinking the links
print("\n\nWe can only invite 3 guests.")
removed_guest = guests.pop()
print(f"\t{removed_guest}, I am sorry I can't invite toy to dinner")
removed_guest = guests.pop()
print(f"\t{removed_guest}, I am sorry I can't invite toy to dinner")
removed_guest = guests.pop()
print(f"\t{removed_guest}, I am sorry I can't invite toy to dinner")
removed_guest = guests.pop()
print(f"\t{removed_guest}, I am sorry I can't invite toy to dinner")

print(guests)
print(f"{guests[0].title()} and {guests[1].title()}, You are still invited to dinner.")

print(f"\nDinner is over.")

del guests[0]
del guests[0]

print(guests)
