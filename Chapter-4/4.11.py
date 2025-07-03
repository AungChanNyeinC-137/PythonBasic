pizzas = ["Seafood Pizza","Veggie Pizza","Pepperoni Pizza"]
friend_pizzas = pizzas[:]
pizzas.append("Spicy Pizza")
friend_pizzas.append("Candy Pizza")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend’s favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)