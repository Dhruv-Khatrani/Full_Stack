#1. Create a Dictionary from Product Names and Prices Using zip()

products = ["Mobile", "Laptop", "Keyboard", "Mouse"]
prices = [15000, 55000, 1200, 500]

product_prices = dict(zip(products, prices))

print(product_prices)
print("*******************************************************")

#2. Create a Dictionary Without Using zip()

usernames = ["raj_07", "ananya_xo", "rahul_123"]
followers = [1500, 3200, 2100]

user_data = {}

for i in range(len(usernames)):
    user_data[usernames[i]] = followers[i]

print(user_data)
print("*******************************************************")

#3. IPL Teams and Points Using zip()

teams = ["CSK", "MI", "GT", "RCB", "KKR"]
points = [12, 8, 14, 10, 16]

team_points = dict(zip(teams, points))

print("Teams with more than 10 points:")

for team, point in team_points.items():
    if point > 10:
        print(team, "-", point)
print("*******************************************************")

#4. Create a List of Movie Dictionaries Using zip()

titles = ["3 Idiots", "Dangal", "Bahubali"]
genres = ["Comedy", "Sports", "Action"]
ratings = [8.4, 8.3, 8.0]

movies = []

for title, genre, rating in zip(titles, genres, ratings):
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    movies.append(movie)

print(movies)
