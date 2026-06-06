class Restaurant:

    def openorder(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total = 0
        print("Hello", customer_name, ", your order ID", order_id, "is created")

    def show_menu(self):
        print("\n------ MENU ------")
        print("1 Pizza  - 200 Rs")
        print("2 Burger - 100 Rs")
        print("3 Pasta  - 150 Rs")
        print("4 Coffee - 80 Rs")
        print("------------------")

    def add_item(self, choice):
        if choice == 1:
            self.total += 200
            print("Pizza added")
        elif choice == 2:
            self.total += 100
            print("Burger added")
        elif choice == 3:
            self.total += 150
            print("Pasta added")
        elif choice == 4:
            self.total += 80
            print("Coffee added")
        else:
            print("Invalid item")

    def show_bill(self):
        print("\nCustomer:", self.customer_name)
        print("Total Bill:", self.total, "Rs")


r1 = Restaurant()
r1.openorder(101, "Dhruv")

while True:
    print("\n" + "*" * 50)
    print("1 Show Menu")
    print("2 Order Item")
    print("3 Show Bill")
    print("4 Exit")
    print("*" * 50)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        r1.show_menu()

    elif choice == 2:
        r1.show_menu()
        item_choice = int(input("Enter item number: "))
        r1.add_item(item_choice)

    elif choice == 3:
        r1.show_bill()

    elif choice == 4:
        print("Thank you for visiting our restaurant")
        print("*" * 50)
        break

    else:
        print("Invalid choice, please try again")
