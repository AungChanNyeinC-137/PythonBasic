file_name ='pi_million_digits.txt'
with open(file_name) as file_obj:
    lines = file_obj.readlines()
    million_digits = ''
    for line in lines:
        million_digits += line.strip()
    print(million_digits[:52]+'...')
    print(len(million_digits))
    