import pygal
from die import Die


dice1 = Die(8)
dice2 = Die(8)

results = [dice1.roll() + dice2.roll() for roll_num in range(2, 5000000)]


#Analyze the results
frequencies = {}
max_results = dice1.num_sides + dice2.num_sides

for value in range(2, max_results + 1):
    frequencies[value] = results.count(value)


#Visualize result
hist = pygal.Bar()
hist.title = "Result for rolling 2 D8"
hist.x_labels = list(frequencies.keys())
hist.x_title = "Values"
hist.y_title = "Frequencies of Values"

hist.add("D8 + D8", list(frequencies.values()))
hist.render_to_file("d8_visuals.svg")

print(list(frequencies.values()))
