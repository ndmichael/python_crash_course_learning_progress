from die import Die
import pygal


die = Die()
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)


#Analyze the result
frequencies = {}

for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies[value] = frequency


# Visualize result
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Results of rolling 1 D6 die 1000 times"
hist.x_labels = list(frequencies.keys())
hist.x_title = "Results"
hist.y_title = "Frequency of Result"
hist.add('D6', list(frequencies.values()))
hist.render_to_file('d6_visual.svg', tooltip=True)


print(list(frequencies.values()))