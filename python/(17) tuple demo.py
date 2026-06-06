t=(1,1.1,2,3,4,"tops",[100,200,300],True,"python",20)

print(t)
print(t.count(1))
print(t.index(20))
print(t[6])
t[6].append(404)
print(t)

print(10 in t)

for i in t:
    print(i)
