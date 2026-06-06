n=input("enter your string :")

count=0
vowels = "aeiou"

for ch in n:
    if ch in vowels:
        count +=1
print("number of vowels",count)

