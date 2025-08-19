class Restaurant():
    def __init__(self,restaurant_name,  cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name.title()} and \nCuisine type is {self.cuisine_type.title()}')
    
    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is currently open')

restaurant = Restaurant('Shwe Kaung', 'Tea Shop')
restaurant1 = Restaurant('Akkaya', 'Tea Shop')
restaurant2 = Restaurant('Botique', 'Coffee Shop')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()