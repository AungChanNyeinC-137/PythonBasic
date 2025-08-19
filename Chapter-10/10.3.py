prompt = " Enter your name"
name = input(prompt)
file_name = 'guest.txt'
with open(file_name,'w') as file_obj:
    file_obj.write(name)