file_name = 'guest_book.txt'
prompt = " Enter your name\n"
prompt += " Enter 'quit' to exit the program "
with open(file_name,'w')as file_obj:
    name = ''
    while name != 'quit':
        name = input(prompt)
        if name != 'quit':
            file_obj.write(name  + "\n" )




