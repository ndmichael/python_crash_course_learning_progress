"""The car classes for both gas and electric car"""

class Car:
    """Representing a car."""
    def __init__(self, make, model, year):
        """Initialize  attributes describe in a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing car mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set on the odometer reading to be given"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


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