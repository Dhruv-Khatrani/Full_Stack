import udf

while True:

    print("*"*50)
    print("1. oddeven")
    print("2. max of two")
    print("3. max of three")
    print("4. fibonacci")
    print("5. prime")
    print("6. exit")
    print("*"*50)

    choice=int(input("enter your choice : "))
    print("*"*50)

    if choice==1:
        a=int(input("enter value :"))
        udf.oddeven(a)
    elif choice==2:
        a=int(input("enter value :"))
        b=int(input("enter value :"))
        udf.maxoftwo(a,b)
    elif choice==3:
        a=int(input("enter value :"))
        b=int(input("enter value :"))
        c=int(input("enter value :"))
        udf.maxofthree(a,b,c)
    elif choice==4:
        a=int(input("enter value :"))
        udf.fibonacci(a)
    elif choice==5:
        a=int(input("enter value :"))
        udf.prime(a)
    elif choice==6:
        print("thank you")
        print("*"*50)
        break
    else:
        print("invalid choice. please try again")
    print("*"*50)
