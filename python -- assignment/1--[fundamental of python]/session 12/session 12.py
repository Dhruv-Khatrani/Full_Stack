#1. Function get_discounted_price()

def get_discounted_price(price, discount_percent):
    final_price = price - (price * discount_percent / 100)
    return final_price

# Test
result = get_discounted_price(500, 10)
print("Discounted Price:", result)
print("***********************************************")

#2. Function format_follower_count()

def format_follower_count(count):
    if count >= 1000000:
        return f"{count/1000000:.1f}M"
    elif count >= 1000:
        return f"{count/1000:.1f}K"
    else:
        return str(count)

# Test
print(format_follower_count(1500))
print(format_follower_count(1200000))
print(format_follower_count(850))
print("***********************************************")

#3. Convert Song Durations to Seconds Using map() and lambda

durations = [3.5, 4.2, 5.0, 2.8]

seconds = list(map(lambda x: x * 60, durations))

print(seconds)
print("***********************************************")

#4. Filter Product Names Starting with 'M'

products = ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']

filtered_products = list(
    filter(lambda product: product.startswith('M'), products)
)

print(filtered_products)
print("***********************************************")

#5. Calculate Total Bill Using reduce() and lambda

from functools import reduce

prices = [120, 80, 150, 60]

total_bill = reduce(lambda x, y: x + y, prices)

print("Total Bill Amount:", total_bill)
