from matplotlib import pyplot as plt

x_values = list(range(1, 100))

y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Reds, edgecolors="none", s=40)

plt.title("My Scatter Square", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Squares values", fontsize=14)

#Set the size of the tick labels
plt.tick_params(axis="both", which="major", labelsize=14)

#Set the range of each axis
# plt.axis([0, 110, 0, 110000])
plt.show()