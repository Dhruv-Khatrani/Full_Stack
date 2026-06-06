for i in range (1,10):
    print("*"*i)


for i in range (1,10):
    print(" "*(9-i),"*"*i)


for i in range (9,0,-1):
    print("*"*i)

for i in range (1,10):
    print(" "*(9-i)," *"*i)


for i in range (9,0,-1):
    print(" "*(9-i)," *"*i)
    

for i in range (1,10):
    print(" "*(9-i),(str(i)+" ")*i)

for i in range (1,10):
    for j in range (1,i+1):
        print(str(j),end="")
    print()


ch = 65 
for i in range (1,5):
    for j in range (i):
        print(chr(ch),end="")
    ch +=1
    print() 
        
