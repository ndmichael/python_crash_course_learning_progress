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
