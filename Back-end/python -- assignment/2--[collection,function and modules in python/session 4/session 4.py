#1. Create a Tuple my_profile
my_profile = (
    "Dhruv",      
    20,           
    "Pizza",      
    True          
)

print(my_profile)
print("*******************************************************")

#2. Print the 2nd, 3rd, and 4th Songs Using Slicing

playlist = (
    'Shape of You',
    'Blinding Lights',
    'Believer',
    'Senorita',
    'Levitating'
)

print(playlist[1:4])
print("*******************************************************")

#3. Convert Tuple to List, Add an Item, and Convert Back

order = ('Burger', 'Fries', 'Coke')

# Convert to list
order_list = list(order)

# Add new item
order_list.append('Ice Cream')

# Convert back to tuple
order = tuple(order_list)

print(order)
print("*******************************************************")

#4. Create a Mixed Tuple insta_post

insta_post = (
    101,                        
    "dhruv_123",                
    250,                        
    ["#travel", "#nature"],     
    True                        
)

print(insta_post)

for item in insta_post:
    print(item, "->", type(item))
print("*******************************************************")

#5. Remove Calls Shorter Than 5 Minutes

call_durations = (12, 5, 0, 20, 7, 3, 15)

# Convert tuple to list
duration_list = list(call_durations)

# Keep only calls that are 5 minutes or longer
filtered_list = []

for duration in duration_list:
    if duration >= 5:
        filtered_list.append(duration)

# Convert back to tuple
result = tuple(filtered_list)

print(result)
