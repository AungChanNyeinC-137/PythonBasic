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

class IcecreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = {"Ice Cream","Chocolate","Vennila"}
    def describe_flavor(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(flavor)
    
ice_cream = IcecreamStand('Kaung Kyawl','Tea shop') 
ice_cream.describe_flavor()


