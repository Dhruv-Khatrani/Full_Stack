class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old."


student = student("bunny",13)
print(student.describe())
