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

    def fill_gas_tank(self):
        print("Filling the gas tank in "+ self.make.title() +" car.")

class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size} kwh battery.')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size > 70:
            range = 270
        message = f"This car can go approximately {range} miles " 
        message += "on full charge" 
        print(message)
    
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            print(f'Your  car battery size has upgraded to {self.battery_size}')
        else:
            print (f'Your car battery size has already upgraded to 85')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery()
    
    # def describe_battery(self):
    #     print(f"This car has a {self.battery_size} kwh battery.")
    
    def fill_gas_tank(self):
        print("Electric car doesn't need a gas tank to fill")


        
electric_car = ElectricCar('ToyoTa', 'V2', 2016)
electric_car.battery_size.get_range()
electric_car.battery_size.upgrade_battery()
electric_car.battery_size.get_range()