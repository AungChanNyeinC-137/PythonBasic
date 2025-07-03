fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Grapes",
    "Strawberry",
    "Pineapple",
    "Mango",
    "Kiwi",
    "Watermelon",
    "Blueberry"
]

print(f'The first three items in the list are:{fruits[0:3]}')
middle = int(len(fruits)/2)
print(f"Three items from the middle of the list are:{fruits[middle-1:middle+2]}")
print(f"The last three items in the list are:{fruits[-3:]}")