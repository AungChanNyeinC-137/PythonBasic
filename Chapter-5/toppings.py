requested_toppings = ['mushrooms', 'extra cheese','pepparoni','pineapple','green peppers']
if 'mushrooms' in requested_toppings:
    print('adding mushrooms to your pizza')
elif 'extra cheese' in requested_toppings:
    print('adding extra cheese to your pizza')
elif 'pepperoni' in requested_toppings:
    print('adding pepperoni to your pizza')
print('Finished making your pizza!')

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f'Sorry we are out of {requested_topping} right now')
    else:
        print(f'adding {requested_topping}.')
print('Finished making your pizza!')

requested_toppings = []
if requested_toppings:
    for requested_toppings in  requested_toppings:
        print(f'adding {requested_topping} in your pizza')
else:
    print('are you sure you want a plain pizza?')


available_toppings = [
    'pepperoni',
    'mushrooms',
    'onions',
    'sausage',
    'bell peppers',
    'olives',
    'extra cheese',
    'pineapple',
    'bacon',
    'jalapenos'
]


requested_toppings = [
    'mushrooms',
    'extra cheese',
    'pepperoni',
    'onions',
    'chilli'
]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping} in your pizza')
    else:
        print(f'Sorry! we do not have {requested_topping} right now!')
print('\n Finished making your pizza')
