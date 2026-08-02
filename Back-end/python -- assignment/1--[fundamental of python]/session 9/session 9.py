#1. Create a List of Favorite Apps

my_fav_apps = ["Instagram", "Zomato", "Spotify", "YouTube", "Paytm"]

print(my_fav_apps)
print("***************************************************************")

#2. Add a New App Using append()

my_fav_apps = ["Instagram", "Zomato", "Spotify", "YouTube", "Paytm"]

my_fav_apps.append("Swiggy")

print(my_fav_apps)
print("***************************************************************")


#3. Insert WhatsApp at the Second Position

my_fav_apps = ["Instagram", "Zomato", "Spotify", "YouTube", "Paytm"]

my_fav_apps.insert(1, "WhatsApp")

print(my_fav_apps)
print("***************************************************************")


#4. Remove an App Using remove() and pop()

my_fav_apps = ["Instagram", "WhatsApp", "Zomato", "Spotify", "YouTube", "Paytm"]


my_fav_apps.remove("Paytm")

print("After remove():", my_fav_apps)


my_fav_apps.pop()

print("After pop():", my_fav_apps)
print("***************************************************************")

#5. Sort and Reverse the List

my_fav_apps = ["Instagram", "WhatsApp", "Zomato", "Spotify"]

my_fav_apps.sort()

print("Alphabetical Order:")
print(my_fav_apps)


my_fav_apps.reverse()

print("\nReverse Order:")
print(my_fav_apps)
