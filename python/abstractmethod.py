from abc import ABC,abstractmethod

class A(ABC):

    @abstractmethod
    def show (self):
        pass

class B(A):

    def show(self):
        print("show difind in class B")
    def display(self):
        print("display from class B")

b1=B()
b1.show()
b1.display()
