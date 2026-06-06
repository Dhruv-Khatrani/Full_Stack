#1. Create a Dictionary playlist and Update a Song Duration

playlist = {
    "Believer": 204,
    "Shape of You": 233,
    "Perfect": 263
}

# Update the duration of a song
playlist["Believer"] = 210

print("Updated Playlist:")
print(playlist)
print("*******************************************************")

#2. Nested Dictionary user_profiles

user_profiles = {
    "raj_07": {
        "followers": 1500,
        "following": 500,
        "posts": 120
    },
    "ananya_xo": {
        "followers": 3200,
        "following": 800,
        "posts": 250
    }
}

print("Followers of ananya_xo:")
print(user_profiles["ananya_xo"]["followers"])
print("*******************************************************")

#3. Zomato-Style Restaurant Menu Using a Nested Dictionary

restaurants = {
    "Pizza Point": {
        "cuisine": "Italian",
        "rating": 4.2
    },
    "Burger Hub": {
        "cuisine": "Fast Food",
        "rating": 4.0
    }
}


restaurants["Burger Hub"]["rating"] = 4.5

print(restaurants)
print("*******************************************************")

#4. Add a New IPL Team and Print Team Captains

team = {
    'CSK': {
        'captain': 'Dhoni',
        'players': 18
    },
    'MI': {
        'captain': 'Rohit',
        'players': 17
    }
}

team['GT'] = {
    'captain': 'Hardik',
    'players': 16
}

for team_name, details in team.items():
    print(team_name, "-", details['captain'])



