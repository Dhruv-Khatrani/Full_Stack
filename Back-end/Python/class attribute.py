class car:
    wheels=4

    def __int__(self,brand,model):
        self.brand = brand
        self.model = model
    def show(self):
        print("brand :",self.brand)
        print("model :",self.model)


car1 = car("toyota","camry")
car2 = car("honda","civic")

car1.show()
car2.show()

print(car1.wheels)
print(car2.wheels)
