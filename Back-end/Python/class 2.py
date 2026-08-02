class Bank:

    def openaccount(self,acno,cname,blance):
        self.acno=acno
        self.cname=cname
        self.blance=blance
        print("hello",cname,"your acount number",acno,"is opened for ",blance,"RS")

    def deposit(self,amount):
        self.blance=self.blance+amount
    def withdraw(self,amount):
        if amount<=self.blance:
            self.blance=self.blance-amount
        else:
            print("sorry you need another",amount-self.blance,"RS to withdraw")
    def checkblance(self):
        print("your current blance is :",self.blance)

b1=Bank()
b1.openaccount(111,"dhruv",5000)

while True:
    print("*"*50)
    print("1 deposit")
    print("2 withdraw")
    print("3 checkblance")
    print("4 exit")
    print("*"*50)

    choice=int(input("enter your choice :"))

    if choice==1:
        amount=int(input("enter deposit amount :"))
        b1.deposit(amount)
    elif choice==2:
        amount=int(input("enter withdraw amount :"))
        b1.withdraw(amount)
    elif  choice==3:
        b1.checkblance()
    elif choice==4:
        print("thank you for using our services")
        print("*"*50)
    else:
        print("invalid choice. plesse trye again")
    print("*"*50)
        
