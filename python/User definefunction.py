#function with no argument & no return value

def printline():
    print("*"*50)

printline()
print("welcome to user define function is python.")
printline()


#function with argument & no return value

def add(a,b):
    print("addition :",a+b)

printline()
x=int(input("enter value :"))
y=int(input("enter value :"))
add(x,y)
printline()


#function with argument & return value

def sub(a,b):
    return a-b

printline()
x=int(input("enter value :"))
y=int(input("enter value :"))
#ans=sub(x,y)
print("subtraction :",sub(x,y))
printline()


