#1. Round Cricket Scores to the Nearest Integer

scores = [56.7, 102.3, 88.9, 45.2, 120.8]

rounded_scores = []

for score in scores:
    rounded_scores.append(round(score))

print("Original Scores:", scores)
print("Rounded Scores:", rounded_scores)
print("*******************************************************")

#2. Sort Restaurant Ratings in Descending Order

ratings = [4.2, 3.8, 4.9, 2.5, 4.0]

sorted_ratings = sorted(ratings, reverse=True)

print("Ratings in Descending Order:")
print(sorted_ratings)
print("*******************************************************")

#3. Sort Flipkart Product Names Alphabetically

products = ["Laptop", "Mobile", "Keyboard", "Monitor", "Mouse"]

products.sort()

print("Sorted Products:")
print(products)
print("*******************************************************")

#4. Pair Restaurant Names with Delivery Times Using zip()

restaurants = ['Burger Hub', 'Pizza Point', 'Sushi House']
delivery_times = [30, 25, 40]

for restaurant, time in zip(restaurants, delivery_times):
    print(f"{restaurant} - {time} min")
print("*******************************************************")

#5. Function to Pair Video Titles with Rounded View Counts

def video_views(titles, views):
    result = []

    for title, view in zip(titles, views):
        rounded_view = round(view, -3)  # Round to nearest thousand
        result.append((title, rounded_view))

    return result

# Example
titles = ["Python Tutorial", "Gaming Highlights", "Travel Vlog"]
views = [15432, 98765, 1204567]

print(video_views(titles, views))
