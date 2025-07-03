cars = ['subaru', 'audi', 'honda', 'bmw', 'land cruiser', 'tesla', 'mercedes', 'toyota', 'nissan', 'jeep']
wrong_car = 'kluger'
right_car = 'subaru'
for car in cars:
    if car.lower() == 'subaru':
        print(car.upper())
    elif car.lower() == 'audi':
        print(car.lower())
    else:
        print(car.title())

age =  10
if (age < 4) and (age > 0 ):
    print('Your admission cost is $0.')
elif (age >= 4) and (age <= 18): 
    print('Your admission cost is $10.')
elif (age == 19) or (age > 19):
    print('Your admission cost is $20.')
else:
    print('your age is not valid')

if right_car in cars:
    print(f'{right_car} is in the list')
else:
     print(f'{right_car} is not in the list')

if wrong_car not in cars:
    print(f'{wrong_car} is not in the list')
else:
     print(f'{wrong_car} is in the list')

