from random import choice

class RandomWalk:
    """A class to generateb random walk"""

    def __init__(self, num_points: int =5000) -> None:
        '''Initialize attributes of a walk'''
        self.num_points = num_points

        #All walks starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''Calculate all then points in a walk'''

        #Kepp taking steps until the point reaches te desired length.
        while len(self.x_values) < self.num_points:
            #Decide which direction to go and how far
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #Rejects moves that goes no where
            if x_step == 0 and y_step == 0:
                continue

            # Clculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)