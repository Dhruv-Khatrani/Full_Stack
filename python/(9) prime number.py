num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
else:
    print(num, "is NOT a prime number")




n=int(input("enter your n :"))

if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print(n,"is not prime")
            break
    else:
        print(n,"is a prime ")
else:
    print(n,"is not prime")
   
