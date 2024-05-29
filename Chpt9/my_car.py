from car import Car, ElectricalCar


    


my_e1 = ElectricalCar('nissan', 'leaf', '2024')
print(my_e1.get_descriptive_name())
# my_e1.describe_battery_life()
my_e1.battery.describe_battery_life()
my_e1.battery.range()
