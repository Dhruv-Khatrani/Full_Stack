print("start of the code......")

try:
    a=int(input("enter your a :"))
    b=int(input("enter your b :"))
    c=a/b
    print("Division : ",c)
    l1 = [12,34,50,60,66]
    index=int(input("enter your index number :"))
    print(l1[index])
    
except Exception as e:
    print("exception caught :",e)
finally:
    print("finally block called")


print("end of the code.......")
