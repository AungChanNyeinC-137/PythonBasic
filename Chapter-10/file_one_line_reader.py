with open('pi_digits.txt') as file_obj:
    lines = file_obj.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
    print(pi_string)
    print(len(pi_string))