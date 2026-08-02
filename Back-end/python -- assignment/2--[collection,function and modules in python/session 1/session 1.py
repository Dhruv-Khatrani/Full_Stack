#1. Create a List fav_items

fav_items = [
    "Believer", 
    20,           
    15.5,         
    True        
]

print(fav_items)
print("***************************************************")

#2. Update the Song Name and Increase Age by 1

fav_items = ["Believer", 20, 15.5, True]

# Change song name
fav_items[0] = "Shape of You"

# Increase age by 1
fav_items[1] = fav_items[1] + 1

print(fav_items)
print("***************************************************")

#3. Remove the Mobile Data Usage Using del

fav_items = ["Shape of You", 21, 15.5, True]


del fav_items[2]

print(fav_items)
print("***************************************************")

#4. Create weekend_plan and Remove the Last Item Using pop()

weekend_plan = [
    "Watch a movie",
    "Play cricket",
    "Go shopping",
    2,            # Hours of exercise
    "Visit friends"
]

removed_item = weekend_plan.pop()

print("Removed Item:", removed_item)
print("Updated List:", weekend_plan)

