l1=["anjali",["prins"],["om"],["asvin"]]

def findvowels(name):
    if name[0] in "aeiou":
        return name

l2 = list(filter(findvowels,l1))
print(l2)
