#1. Print Names of Five Food Delivery Apps Using a for Loop

apps = ["Zomato", "Swiggy", "Domino's", "McDonald's", "Pizza Hut"]

for app in apps:
    print(app)
print("******************************************************************")

#2. Count Characters in a User Bio (Excluding Spaces)

user_bio = "Music lover | Foodie | Traveller"

count = 0

for char in user_bio:
    if char != " ":
        count += 1

print("Number of characters (excluding spaces):", count)
print("******************************************************************")

#3. Print Favorite Movies in Uppercase

fav_movies = ["3 Idiots", "Dangal", "Bahubali"]

for movie in fav_movies:
    print(movie.upper())
print("******************************************************************")

#4. Print Only Vowels from a Word

word = input("Enter a word or song name: ")

for char in word:
    if char.lower() in "aeiou":
        print(char)
