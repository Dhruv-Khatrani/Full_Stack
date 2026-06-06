
ch = 65 
for i in range (1,5):
    for j in range (i):
        print(chr(ch),end="")
    ch +=1
    print() 
print("*******************************")        

ch = 69 
for i in range (5,0,-1):
    for j in range (i):
        print(chr(ch),end="")
    ch -=1
    print()
print("*******************************")        

for i in range(1, 5):
    for j in range(i):
        print(chr(65 + j), end="")
    print()    
print("*******************************")        


