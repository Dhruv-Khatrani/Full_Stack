#1. Function calculate_total()

def calculate_total(price, quantity):
    return price * quantity

result = calculate_total(120, 3)

print("Total Amount:", result)
print("*******************************************************")

#2. Function format_username()

def format_username(username, prefix="user_"):
    return prefix + username

print(format_username("dhruv"))

print(format_username("dhruv", "insta_"))
print("*******************************************************")

#3. Function book_movie_ticket()

def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    print("Movie:", movie_name)
    print("Seat Type:", seat_type)
    print("Snacks:", snacks)
    print("-" * 20)

# Only positional arguments
book_movie_ticket("Jawan", "VIP", "Popcorn")

# Only keyword arguments
book_movie_ticket(
    movie_name="Pathaan",
    seat_type="Premium",
    snacks="Cold Drink"
)

# Mix of positional and keyword arguments
book_movie_ticket(
    "Jawan",
    snacks="Popcorn",
    seat_type="VIP"
)
print("*******************************************************")

#4. Function apply_coupon()

def apply_coupon(amount, coupon_code=None):
    if coupon_code == "SAVE10":
        return amount * 0.90   # 10% discount
    return amount

print("Final Amount:", apply_coupon(1000))

print("Final Amount:", apply_coupon(1000, "SAVE10"))

