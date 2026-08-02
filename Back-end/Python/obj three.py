class student:
    subject= "python"

    def __init__(self,name,age):
        self.name = name
        self.age  = age

    @classmethod
    def get_subject(cls):
        return cls.subject

    @staticmethod
    def add (x,y):
        return x+y

a=student(abc,20)
print(student.get_subject())

