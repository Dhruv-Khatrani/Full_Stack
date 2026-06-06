from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(self,r):
        pass

class SBI():

    def roi(self,r):
        print("rate of interest given by sbi is :",r)

class HDFC(RBI):

    def roi(self,r):
        print("rate of interest given by sbi is :",r)

s1=SBI()
s1.roi(6.1)

h1=HDFC()
h1.roi(7.2)
