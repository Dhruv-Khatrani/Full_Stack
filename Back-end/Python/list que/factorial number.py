n=int(input("enter your n :"))

factorial=1

for i in range(1,n+1):
    factorial *=i
    print("factorial of",n,"is",factorial)
