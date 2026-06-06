class restaurant:

    def openorder(self, order_id, cname):
        self.order_id=order_id
        self.cname=cname
        print("hello",cname,"your order id",order_id,"is created")

    def show_manu(self):
        print("\n-----manu-----")
        print("1 pizza - 200rs")
        print("2 burger- 100rs")
        print("3 pasta - 150rs")
        print("4 coffee - 80rs")

    def add_item(self,choice):
        if choice == 1:
            self.total += 200
            print("pizza added")
        elif choice == 2:
            self.total +=100
            print("burger added")
        elif choice == 3:
            self.total +=150
            print("pasta added")
        elif choice == 4:
            self.total +=80
            print("coffee added")
    def show_bill(self):
        print("customer order:",self.)
    

 r1 = resturant()
 r1.openorder(100,"dhruv")

 while True:
     print("*"*50)
     print("1 ")
     
