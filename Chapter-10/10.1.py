file_name = 'learning_python.txt'
with open(file_name) as file_obj:
    print("Whole Object")
    contents = file_obj.read()
    print(contents)

with open(file_name) as file_obj:
    print("line by line")
    for line in file_obj:
        print(line)

with open(file_name) as file_obj:   
    print(("by list"))
    lessons = file_obj.readlines()
    for lesson in lessons:
        print(lesson.rstrip())