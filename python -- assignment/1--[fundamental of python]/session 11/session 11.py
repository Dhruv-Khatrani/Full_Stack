#1. Create a Dictionary my_playlist

my_playlist = {
    "Believer": 3.5,
    "Shape of You": 4.2,
    "Perfect": 4.5
}

print(my_playlist)
print("****************************************************")
#2. Add a New Song and Update an Existing Song

my_playlist = {
    "Believer": 3.5,
    "Shape of You": 4.2,
    "Perfect": 4.5
}

my_playlist["Blinding Lights"] = 3.8

my_playlist["Believer"] = 3.7

print(my_playlist)
print("****************************************************")

#3. Function display_friends()

def display_friends(friends):
    for username, followers in friends.items():
        print(f"{username}: {followers/1000:.1f}K followers")

# Example
friends = {
    "priya_123": 2300,
    "rahul_official": 5800,
    "music_lover": 1200
}

display_friends(friends)
print("****************************************************")

#4. Using keys(), values(), and items()

food_order = {
    'Pizza': 2,
    'Burger': 1,
    'Fries': 3
}

# a) All food items
print("Food Items:")
for item in food_order.keys():
    print(item)

# b) All quantities
print("\nQuantities:")
for qty in food_order.values():
    print(qty)

# c) Item with quantity
print("\nItems and Quantities:")
for item, qty in food_order.items():
    print(item, ":", qty)
print("****************************************************")

#5. Function update_cart(cart, item, qty)

def update_cart(cart, item, qty):
    if item in cart:
        cart[item] += qty
    else:
        cart[item] = qty

    return cart

# Example
cart = {
    "Mobile": 1,
    "Headphones": 2
}

print(update_cart(cart, "Mobile", 1))
print(update_cart(cart, "Charger", 2))
