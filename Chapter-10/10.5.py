file_name = 'reasons.txt'
prompt = " Enter why you like programming\n"
prompt += " Enter 'quit' to exit the program "
with open(file_name,'w')as file_obj:
    reason = ''
    while reason != 'quit':
        reason = input(prompt)
        if reason != 'quit':
            file_obj.write(reason  + "\n" )




