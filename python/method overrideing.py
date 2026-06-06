class A:
    def show(self):        
        print("show from class a")
class B(A):
    def show(self):
        super().show()
        print("show from class b")
class C(B):
    def show(self):
        super().show()
        print("show from class C")
class D(C,B):
    def show(self):
        super().show()
        print("show from class D")

d1=D()
d1.show()
