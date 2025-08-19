class User():
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'User name is {self.first_name.title()} {self.last_name.title()}')
    def greet_user(self):
        print(f'Hello {self.first_name.title()} {self.last_name.title()}')

user = User('Aung' ,'Chan')
user.describe_user()
user.greet_user()