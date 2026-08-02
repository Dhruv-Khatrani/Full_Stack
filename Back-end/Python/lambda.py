x=lambda a,b,c:a+b+c
print("addition :",x(10,20,30))

result = lambda num : "even" if num%2==0 else "odd"
print(result(12))


result = lambda num : num*num
print(result(4))

result = lambda num : num*num*num
print(result(5))


result = lambda a,b:"a is max" if a>b else "b is max"
print(result(6,7))
