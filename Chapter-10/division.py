prompt = "Give me two numbers. I'll divide them."
prompt += "Enter 'q' to quit."
print(prompt)
while True:
    f_number = input("Enter first number: ")
    if f_number == 'q': 
        break
    s_number = input("Enter second number:")
    if s_number == 'q':
        break
    try: 
        answer = int(f_number)/ int(s_number)
    except ZeroDivisionError:
        print("You Can't divide with 0 ")
    else:
        print(answer)
   