class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"{self.name} serves lovely {self.type}.")

    def open_restaurant(self):
        print("restuarant is open.")


restaurant1 = Restaurant("Sea side", "seafood")
restaurant2 = Restaurant("Marakki", "Italian food")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()