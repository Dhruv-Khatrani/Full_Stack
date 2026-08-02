#1. Dynamic Nested Dictionary for a Flipkart Shopping Cart
cart = {}

# User 1
cart["rahul"] = {
    "items": [
        {"name": "Mobile", "quantity": 1, "price": 15000},
        {"name": "Headphones", "quantity": 2, "price": 1200}
    ]
}

# User 2
cart["priya"] = {
    "items": [
        {"name": "Laptop", "quantity": 1, "price": 55000},
        {"name": "Mouse", "quantity": 1, "price": 500}
    ]
}

print(cart)
print("*******************************************************")

#2. Function add_song_to_playlist()

def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    # Create user if missing
    playlists.setdefault(user, {})

    # Create playlist if missing
    playlists[user].setdefault(playlist_name, [])

    # Add song
    playlists[user][playlist_name].append({
        "title": song_title,
        "artist": artist
    })

    return playlists


playlists = {}

add_song_to_playlist(
    playlists,
    "rahul",
    "Favorites",
    "Believer",
    "Imagine Dragons"
)

add_song_to_playlist(
    playlists,
    "rahul",
    "Favorites",
    "Shape of You",
    "Ed Sheeran"
)

add_song_to_playlist(
    playlists,
    "priya",
    "Workout",
    "Levitating",
    "Dua Lipa"
)

print(playlists)
print("*******************************************************")

#3. Dynamic IPL Team Scores Dictionary

ipl_scores = {}

ipl_scores["CSK"] = {
    "Dhoni": 45,
    "Jadeja": 38,
    "Gaikwad": 72
}

ipl_scores["MI"] = {
    "Rohit": 65,
    "Surya": 54,
    "Tilak": 30
}

# Print runs of a specific player
print("Rohit's Runs:", ipl_scores["MI"]["Rohit"])
print("*******************************************************")

#4. Zomato Orders Functions

orders = {}

def add_order(orders, order_id, restaurant, items, total):
    orders.setdefault(order_id, {})
    orders[order_id]["restaurant"] = restaurant
    orders[order_id]["items"] = items
    orders[order_id]["total"] = total


def update_total(orders, order_id, new_total):
    if order_id in orders:
        orders[order_id]["total"] = new_total


# Add orders
add_order(
    orders,
    101,
    "Pizza Point",
    ["Pizza", "Coke"],
    450
)

add_order(
    orders,
    102,
    "Burger Hub",
    ["Burger", "Fries"],
    300
)

# Update total
update_total(orders, 101, 500)

print(orders)
print("*******************************************************")

#5. Refactor to Avoid KeyError

playlists = {
    'user1': {
        'Favourites': ['Song1', 'Song2']
    }
}

playlists.setdefault('user2', {})
playlists['user2'].setdefault('Chill', [])

playlists['user2']['Chill'].append('Song3')

print(playlists)
