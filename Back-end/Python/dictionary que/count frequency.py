number =[1,2,2,3,4,1,2]

freq = {}

for i in number:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] =1
print(freq)
