from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(self,r):
        pass
class SBI(RBI):

    def show(self):
        print("i am sbi")
    def roi(self,r):
        print("rate of interest given by sbi is :",r)

class HDFC(RBI):

    def show(self):
        print("i am HDFC")
    def roi(self,r):
        print("rate of interest given by sbi is :",r) 

s1=SBI()
s1.show()
s1.roi()
