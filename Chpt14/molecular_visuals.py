from matplotlib import pyplot as plt
from random_walk import RandomWalk



#Making a  random walk and plot the points
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.figure(figsize=(9, 4))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, c='purple', linewidth=5)


    plt.show()

    keep_running = input("Make another walk? {y/n}: ")
    if keep_running in ['n', 'N']:
        break