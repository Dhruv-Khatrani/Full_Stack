class car:
    wheels=4

    def __int__(self,brand,model):
        self.brand = brand
        self.model = model


car1 = car("toyota","camry")
car2 = car("hond","civic")

print(car1.wheels)
print(car2.wheels)
