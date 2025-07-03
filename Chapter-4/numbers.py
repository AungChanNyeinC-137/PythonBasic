for value in range(1,5):
    print(value)
for value in range(1,6):
    print(value)
numbers = list(range(1,11))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for square in range(1,11):
    value = square**2
    squares.append(value)
print(squares)

squares1 = []
for square in range(1,11):
    squares1.append(square*square)
print(squares1)

print(f"{min(numbers)}\n")
print(f"{max(numbers)}\n")
print(f"{sum(numbers)}\n")

#list comprehension
tubes = [value**3 for value in range(1,11)]
print(tubes)

squaresz = [value**2 for value in range(1,50)]
print(squaresz)