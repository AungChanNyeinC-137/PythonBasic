print('Enter age')
age = float(input())
if age < 2:
    print('This person is a baby')
elif age >= 2 and age < 4:
    print('This person is a toddler')
elif age >= 4 and age < 13:
    print('This person is a kid')
elif age >= 13 and age < 20:
    print('This person is a teenager')
elif age >= 20 and age < 65:
    print('This person is a adult')
elif age >65:
    print('This person is an elder')