d1={'a':10,'b':20,'c':30}
d2={'a':60,'c':90,'e':78}
d3={}


for i in d1:
    if i in d2:
        d3[i]=d1[i]+d2[i]
       
print(d3)
