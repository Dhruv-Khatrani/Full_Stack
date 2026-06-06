#1. Generate Even Numbers Between 10 and 50 Using List Comprehension
even_numbers = [num for num in range(10, 51) if num % 2 == 0]

print(even_numbers)
print("*******************************************************")

#2. Get Song Durations Greater Than 200 Seconds

playlists = [
    [210, 180, 240],
    [150, 200],
    [300, 120, 90]
]

long_songs = [
    duration
    for playlist in playlists
    for duration in playlist
    if duration > 200
]

print(long_songs)
print("*******************************************************")


#3. Create Product-Price Tuples for Products Above ₹1000

names = ['Shoes', 'Bag', 'Watch', 'Headphones']
prices = [999, 1500, 700, 2200]

expensive_products = [
    (name, price)
    for name, price in zip(names, prices)
    if price > 1000
]

print(expensive_products)
print("*******************************************************")

#4. Flatten a Restaurant Rating Matrix and Get Ratings Above 4

ratings = [
    [4, 5, 3, 2],
    [5, 4, 4, 3],
    [3, 2, 5, 5]
]

high_ratings = [
    rating
    for row in ratings
    for rating in row
    if rating > 4
]

print(high_ratings)

