#student class created
class Student:
    #intials function with attributes of STudent class
    def __init__(self, name, school_id, gpa):
        #set objects to variable
        self.name = name
        self.school_id= school_id
        self.gpa = gpa

    # string function
    def __str__(self):
        return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'


Student1=Student('abdi', 6256, 3.4)
Student2=Student('awali', 1234, 2.9)
Student3=Student('jim', '4758', 4.0)
Student4=Student('pam', 910, 3.8)

print(Student1)
print(Student2)
print(Student3)
print(Student4)
    
