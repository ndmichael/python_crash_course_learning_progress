from matplotlib import pyplot as plt
from random_walk import RandomWalk



#Making a  random walk and plot the points
while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Reds,  s=15)
    plt.show()

    keep_running = input("Make another walk: ")
    if keep_running in ['n', 'N']:
        break