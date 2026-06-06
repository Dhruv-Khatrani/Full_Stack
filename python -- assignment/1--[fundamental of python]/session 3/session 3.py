#1. Welcome Message with Name and Favorite Food

name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")

print("Hello", name + ", your favorite food is", favorite_food + "!")
print("**********************************************************************")

#2. Arithmetic Operations on Two Numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", num1 + num2)
print("Difference =", num1 - num2)
print("Product =", num1 * num2)
print("Quotient =", num1 / num2)
print("**********************************************************************")

#3. Zomato-Style Bill Calculator

price = float(input("Enter food item price: ₹"))
quantity = int(input("Enter quantity: "))

total_bill = price * quantity

print("Your total bill is ₹", total_bill)
print("**********************************************************************")

#4. Instagram Follower Count Formatter

followers = int(input("Enter your Instagram follower count: "))

print("\n\tYou have", format(followers, ","), "followers")
print("**********************************************************************")

#5. Basic Calculator Program

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Error: Invalid operator entered.")
    
