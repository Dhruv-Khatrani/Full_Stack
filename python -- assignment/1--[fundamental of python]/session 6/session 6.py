#1. Print Numbers from 1 to 10 Using a while Loop

num = 1

while num <= 10:
    print(num)
    num += 1
print("************************************************")

#2. Zomato-Style Offer Countdown

minutes_left = 5

while minutes_left > 0:
    print("Offer ends in", minutes_left, "minutes")
    minutes_left -= 1

print("Offer expired!")
print("************************************************")

#3. Right-Angled Triangle Star Pattern (5 Rows)

row = 1

while row <= 5:
    print("*" * row)
    row += 1
print("************************************************")

#4. Loading Spinner Using while True

count = 0

while True:
    print("Loading...")
    count += 1

    if count == 3:
        break

print("Loading Complete!")
print("************************************************")

#5. Pyramid Star Pattern (4 Rows)

row = 1

while row <= 4:
    stars = 2 * row - 1
    print("*" * stars)
    row += 1

    
