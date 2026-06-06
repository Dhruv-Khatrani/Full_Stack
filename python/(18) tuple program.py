t=(1,1.1,2,3,4,"tops",[100,200,300],True,"python",20)

num=int(input("enter your t :"))

for i in t:    
     if i==num:
         print(num,"is in tuple")
         break
else:
    print(num,"is not in tuple")
