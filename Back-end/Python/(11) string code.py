s=input("Enter String:")
print("your string : ",s)

al=0
nm=0f
sp=0
uc=0
lc=0

for i in s:
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1

print("Total alphabets :",al)
print("Total numarics :",nm)
print("Total spaces :",sp)
print("Total upper case:",uc)
print("Total lower case :",lc)
    
