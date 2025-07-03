# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car != 'subaru':
#         print(car.upper())
#     else:
#         print(car.lower())

# answer =  12
# print("Guess the number:\n")
# guess_number = float(input())
# if answer!= guess_number:
#     print("Wrong number: guess again")
# else:
#     print("you got it right!")

# age_0 =  21
# age_1 = 18
# if  age_0 == 21 and age_1 == 118:
#     print(True)
# else:
#     print(False)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
ingredient = 'onions'
if ingredient in requested_toppings:
    print(ingredient.title() + " is in requested toppings")
else:
    print(ingredient.title() + "is not in requested toppings")
