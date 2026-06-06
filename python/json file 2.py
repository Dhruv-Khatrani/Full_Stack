import json

users_data = []
num_users = int(input("enter the number of users:"))

for n in range(num_users):
    user_data = {}
    user_data ["name"] = input("enter your name :")
    user_data ["age"] = int(input("enter your age :"))
    user_data ["city"] = input("enter your city :")

    users_data.append(user_data)

with open("user_data.json","w") as file:
    json.dump(user_data,file,indent=4)
print("all users data has been written to users_data.json ")

