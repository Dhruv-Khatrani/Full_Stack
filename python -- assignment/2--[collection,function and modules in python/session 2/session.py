#1. Print Songs with Their Position in the Playlist

playlist = [
    "Believer",
    "Shape of You",
    "Perfect",
    "Blinding Lights",
    "Levitating"
]

position = 1

for song in playlist:
    print(position, "-", song)
    position += 1
print("*********************************************************")

#2. Print Only the First Three Food Items Using range()

foods = ['Pizza', 'Burger', 'Dosa', 'Pasta', 'Fries']

for i in range(3):
    print(foods[i])
print("*********************************************************")

#3. Calculate Total Cart Value

prices = [299, 499, 150, 1200, 350]

total = 0

for price in prices:
    total += price

print("Total Cart Value: ₹", total)
print("*********************************************************")

#4. WhatsApp-Style Unread Messages Counter

unread_counts = [2, 0, 15, 120, 5]

for count in unread_counts:
    if count > 99:
        print("99+")
    else:
        print(count)
