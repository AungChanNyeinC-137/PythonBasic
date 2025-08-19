with open('pi_digits.txt') as file_obj:
    lines = file_obj.readlines()
    for line in lines:
        print(line.rstrip())