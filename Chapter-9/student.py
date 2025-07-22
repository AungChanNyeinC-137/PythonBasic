class Student():
    def __init__(self,name, MKPT, email):
        self.name = name
        self.MKPT = MKPT
        self.email = email
    def info(self):
        print(f"Name: {self.name.title()}\n MKPT: {str(self.MKPT).upper()} \n Email: {self.email}\n")

student1 = Student('Aung Aung', 7362, 'eg@gmail.com')
student2 = Student('Mg Mg', 7363, 'mm@gmail.com')
student3 = Student('David', 7364, 'dv@gmail.com')

print (student1.name)
student1.info()
print (student2.name)
student2.info()
print (student3.name)
student3.info()