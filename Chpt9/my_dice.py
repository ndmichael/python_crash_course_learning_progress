from random import randint


class Dice:

    def __init__(self, sides: int =6) -> None:
        self.sides = sides
        
    def roll_dice(self):
        print(randint(1, self.sides))

roll1 = Dice()
for i in range(10):
    roll1.roll_dice()
