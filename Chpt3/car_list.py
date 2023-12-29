bicycles = ['honda', 'benz', 'peaguot', 'bmw', 'toyota', 'lexus', 'tesla', 'bentley']
friends = ['jamal komadugu', 'tahir anyatullah', 'daniela', 'rose left', 'chukwujekwu', 'toba']
motocycles = ['honda', 'yamaha', 'suzuki']

# print a car with a message
print(f"My first car was a {bicycles[4].title()}.")

for friend in friends:
    print(f"I love you, {friend.title()}.")


# modifying a list
print("\nModifying List")
print(motocycles)
# motocycles[0] = 'ducati'
# print(motocycles)

# add new item or element to a list
motocycles.append('ducati')
print(motocycles)



