import random as rd

class Die():
    """A class representing a single die"""

    def __init__(self, num_sides: int = 6) -> None:
        self.num_sides = num_sides

    def roll(self):
        '''return a random number between 1 to number of sides'''
        return rd.randint(1, self.num_sides)
        