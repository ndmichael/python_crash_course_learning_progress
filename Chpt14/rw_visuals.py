from matplotlib import pyplot as plt
from random_walk import RandomWalk



#Making a  random walk and plot the points
while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=15)

    #Emphasize the first and last points"
    plt.scatter(0,0, c="green", edgecolors="none", s=200)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="purple", edgecolors='red', s=200)
    plt.show()

    keep_running = input("Make another walk: ")
    if keep_running in ['n', 'N']:
        break