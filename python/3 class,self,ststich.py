class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


    @staticmethod
    def school_name():
        print("School: ABC High School")



s1 = Student("Dhruv", 85)
s2 = Student("Rahul", 90)


s1.display()
print()
s2.display()

print()

Student.school_name()
