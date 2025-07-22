class Car():
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reding = 0

    def get_descriptive_name(self):
        long_name =  str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

my_new_car = Car('Sweedin', 'Z', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reding = 823
print(f"This car has {str(my_new_car.odometer_reding)} miles on it")