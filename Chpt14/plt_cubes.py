from matplotlib import pyplot as plt

num_cubes = list(range(1, 5001))
cubes = [x**3 for x in num_cubes]

plt.plot(num_cubes, cubes, c='green')

#set attributes to plot
plt.title("My cube graph", fontsize=22)
plt.xlabel("Cube numbers", fontsize=14)
plt.ylabel("Cubes values", fontsize=14)

#Set size of tick label
plt.tick_params(axis="both", labelsize=8)

#Set the range of each axis
# plt.axis([0, 5100, 0, 5100000])

plt.show()