#1. Create a Tuple of Favorite Apps
fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")

print(fav_apps)
print("******************************************************************")

#2. Access the 2nd and 4th App Using Indexing
fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")

print("2nd App:", fav_apps[1])
print("4th App:", fav_apps[3])
print("******************************************************************")

#3. Attempt to Change a Tuple Element

fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")

fav_apps[0] = "YouTube"
print("******************************************************************")

#4. Print the Middle Three Apps Using Tuple Slicing

fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")

middle_apps = fav_apps[1:4]

print(middle_apps)
print("******************************************************************")

#5. Concatenate Two Tuples

fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")

new_apps = ("Telegram", "Netflix")

all_apps = fav_apps + new_apps

print(all_apps)
