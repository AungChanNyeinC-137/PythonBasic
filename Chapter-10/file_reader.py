# with open("pi_digits.txt") as file_object:
#     contents = file_object.read()
#     print(contents+'\n')
#     print(contents.rstrip())
file_path = 'pi_digits.txt'
with open(file_path) as file_obj:
    contents = file_obj.read()
    print(contents.rstrip())