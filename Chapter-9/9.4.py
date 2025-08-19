class Restaurant():
    def __init__(self,restaurant_name,  cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name.title()} and \nCuisine type is {self.cuisine_type.title()}')
    
    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is currently open')
    
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number
res = Restaurant('Kaung Kywal', 'Chit Tee')
res.describe_restaurant()
res.open_restaurant()
res.set_number_served(5)
res.increment_number_served(4)
print(res.number_served)