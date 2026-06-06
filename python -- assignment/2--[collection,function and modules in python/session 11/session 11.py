#1. Calculate Square Roots Using math.sqrt()

import math

print("Square root of 16 =", math.sqrt(16))
print("Square root of 49 =", math.sqrt(49))
print("Square root of 81 =", math.sqrt(81))
print("*******************************************************")

#2. Flipkart-Style Price Rounder Using math.ceil()

import math

prices = [199.1, 349.8, 599.3]

for price in prices:
    print(f"Original Price: {price}")
    print(f"Rounded Price: {math.ceil(price)}")
print("*******************************************************")

#3. Zomato Bill Calculator Using math.floor()

import math

bill_amount = 799

discounted_bill = bill_amount * 0.90  # 10% discount

final_bill = math.floor(discounted_bill)

print("Final Bill Amount: ₹", final_bill)
print("*******************************************************")

#4. Simulate a Dice Roll Using random.randint()

import random

dice_roll = random.randint(1, 6)

print("Dice Roll:", dice_roll)
print("*******************************************************")

#5. Spotify-Style Daily Playlist Shuffle

import random

songs = [
    "Kesariya",
    "Believer",
    "Shape of You",
    "Perfect",
    "Levitating",
    "Blinding Lights",
    "Senorita",
    "Calm Down"
]

today_playlist = random.sample(songs, 3)

print("Today's Playlist:")

for song in today_playlist:
    print(song)
    
