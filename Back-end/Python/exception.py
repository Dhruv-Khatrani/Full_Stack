print("start of the code......")

try:
    a=int(input("enter your a :"))
    b=int(input("enter your b :"))
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("exception caught")

print("end of the code.......")
