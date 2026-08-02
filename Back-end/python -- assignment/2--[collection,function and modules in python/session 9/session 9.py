#1. Lambda Function to Calculate the Square of a Number

square = lambda x: x ** 2

for i in range(1, 6):
    print(square(i))
print("*******************************************************")

#2. Add a 10% Service Charge Using map() and lambda

prices = [120, 250, 99, 180, 310]

updated_prices = list(map(lambda price: price * 1.10, prices))

print(updated_prices)
print("*******************************************************")

#3. Filter Usernames with More Than 1000 Followers

users = [
    ('raj', 800),
    ('simran', 1500),
    ('veer', 1200),
    ('ananya', 950)
]

popular_users = list(
    filter(lambda user: user[1] > 1000, users)
)

for username, followers in popular_users:
    print(username)
print("*******************************************************")

#4. Lambda Function Returning Sum and Product

calculate = lambda a, b: (a + b, a * b)

print(calculate(3, 4))
print(calculate(5, 2))
print(calculate(7, 8))
print("*******************************************************")

#5. Lambda Function to Check a Palindrome

is_palindrome = lambda text: text == text[::-1]

print("madam:", is_palindrome("madam"))
print("python:", is_palindrome("python"))
print("noon:", is_palindrome("noon"))
