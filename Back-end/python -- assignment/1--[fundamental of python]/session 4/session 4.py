#1. Instagram Account Eligibility Check

age = int(input("Enter your age: "))

if age >= 13:
    print("You are eligible to create an Instagram account.")
else:
    print("You are not eligible to create an Instagram account.")
print("****************************************************************")
#2. Marks and Grade Calculator

marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")
print("****************************************************************")


#3. Zomato Late-Night Order Checker (Nested if)


age = int(input("Enter your age: "))
time = int(input("Enter current time (0-23): "))

if age >= 18:
    if time >= 22 or time <= 2:
        print("Order allowed")
    else:
        print("Order not allowed")
else:
    print("Order not allowed")
print("****************************************************************")


#4. Cricket Team Score Analyzer

score = int(input("Enter your favorite cricket team's score: "))

if score >= 200:
    print("High Score!")
elif score >= 150:
    print("Good Score")
elif score >= 100:
    print("Average")
else:
    print("Needs Improvement")
