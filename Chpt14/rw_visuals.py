from matplotlib import pyplot as plt
from random_walk import RandomWalk



#Making a  random walk and plot the points
while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk: ")
    if keep_running in ['n', 'N']:
        break