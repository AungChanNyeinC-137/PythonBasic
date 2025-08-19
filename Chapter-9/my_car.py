from car import Car
my_new_car = Car('suzuki','V2',2015)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reding = 709
my_new_car.read_odometer()