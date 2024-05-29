from car import Car
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery_life(self):
        """Describing battery life when called"""
        print(f"this car have a battery of {self.battery_size} km/h")

    def range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 250

        print(f"This car can go about {range} miles on a full charge.")

class ElectricalCar(Car):
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery_size = 40
        self.battery = Battery()

    


my_e1 = ElectricalCar('nissan', 'leaf', '2024')
print(my_e1.get_descriptive_name())
# my_e1.describe_battery_life()
my_e1.battery.describe_battery_life()
my_e1.battery.range()
