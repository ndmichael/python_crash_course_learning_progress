from die import Die
import pygal


die1 = Die()
die2 = Die()

results = []

for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)


#Analyze the result
frequencies = {}
max_results = die1.num_sides + die2.num_sides

for value in range(1, max_results + 1):
    frequency = results.count(value)
    frequencies[value] = frequency


# Visualize result
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Results of rolling 1 D6 die 1000 times"
hist.x_labels = list(frequencies.keys())
hist.x_title = "Results"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6', list(frequencies.values()))
hist.render_to_file('dice_visual.svg', tooltip=True)


print(list(frequencies.values()))