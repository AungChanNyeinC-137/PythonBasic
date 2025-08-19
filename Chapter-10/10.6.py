first_number = input("Enter first number ")
second_number = input("Enter second number ")
try: result = first_number / second_number
except TypeError:
    msg = "Only Numbers Allowed to divide"
    print(msg)
else: print(result)