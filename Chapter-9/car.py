class Car():
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reding = 0

    def get_descriptive_name(self):
        long_name =  str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    
    def update_odomenter(self,mileage):
        if(mileage>self.odometer_reding):
            self.odometer_reding = mileage
        else:
            print("you can't roll back odometer")

    def increment_odometer(self,mileage):
        self.odometer_reding += mileage

    def read_odometer(self):
        print(f"This car has {str(self.odometer_reding)} miles on it")

my_new_car = Car('Sweedin', 'Z', 2020)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reding = 823
my_new_car.update_odomenter(1000)
print(my_new_car.odometer_reding)

my_new_car.increment_odometer(50)
print('After updating '+str(my_new_car.odometer_reding))
