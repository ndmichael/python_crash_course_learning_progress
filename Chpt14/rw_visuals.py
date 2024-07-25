from matplotlib import pyplot as plt
from random_walk import RandomWalk



#Making a  random walk and plot the points
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=5)

    #Emphasize the first and last points"
    plt.scatter(0,0, c="green", edgecolors="none", s=200)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="purple", edgecolors='red', s=200)

    #Remove the axis
    # plt.axes().get_yaxis().set_visible(False)
    # plt.axes().set_xticks([])
    # plt.axes().set_yticks([])

    plt.show()

    keep_running = input("Make another walk? {y/n}: ")
    if keep_running in ['n', 'N']:
        break