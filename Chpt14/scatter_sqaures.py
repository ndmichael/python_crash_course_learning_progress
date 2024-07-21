from matplotlib import pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)

plt.title("My Scatter Square", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Squares values", fontsize=14)

#Set the size of the tick labels
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()