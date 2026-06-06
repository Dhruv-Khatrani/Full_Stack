d={190:"dhruv",878:"jay",738:"sarthak",505:"vikash"}

print(d)
print(d[190])
print(d.get(878))
print(d.items())
print(d.key())
print(d.values())
print(d.pop(738))
print(d)
print(d.popitems())
print(d)
d1={555:"mayank",568:"raj",232:"manan"}
d.update(d1)
print(d)
d[555]="ajay"
print(d)

for i in d:
    print(i," : ",d[i])
