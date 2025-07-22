class Dog():
    def __init__(self,name,age):
        self.n = name
        self.a = age
    def sit(self):
        print(self.n+' is sitting')
    def roll_over(self):
        print(self.n+' just rolled over\n')

dog_1 = Dog('Ozu',4)
print(dog_1.n)
print('Age:' + str(dog_1.a))
dog_1.sit()
dog_1.roll_over()

dog_2 = Dog('Minamomo',24)
print(dog_2.n)
print('Age:' + str(dog_2.a))
dog_2.sit()
dog_2.roll_over()

dog_3 = Dog('Aung Net',9)
print('Age:' + str(dog_3.a))
dog_3.sit()
dog_3.roll_over()