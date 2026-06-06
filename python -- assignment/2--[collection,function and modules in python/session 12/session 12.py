#1. Create a Package musicplayer
# musicplayer/player.py

def play_song():
    print("Playing song...")

from musicplayer.player import play_song

play_song()
print("*******************************************************")

#2. Create the foodorder Package

def get_menu():
    return ["Pizza", "Burger", "Pasta", "Fries"]

def place_order(item):
    print("Order placed for:", item)

from .menu import get_menu
from .order import place_order
from foodorder import get_menu, place_order

print(get_menu())

place_order("Pizza")
print("*******************************************************")

#3. Refactor the shoppingcart Package

def add_to_cart(item):
    print(f"{item} added to cart")
    from .cart import add_to_cart
print("*******************************************************")

#4. Create the instahelpers Package

def format_likes(count):
    if count >= 1_000_000:
        return f"{count/1_000_000:.1f}M"
    elif count >= 1_000:
        return f"{count/1_000:.1f}K"
    else:
        return str(count)
from .formatter import format_likes
from instahelpers import format_likes

print(format_likes(500))
print(format_likes(1200))
print(format_likes(1500000))
print("*******************************************************")

#5. Create the ticketbooking Package

def search_event(event_name):
    print(f"Searching for event: {event_name}")

def book_ticket(event_name):
    print(f"Ticket booked for: {event_name}")

from .search import search_event
from .booking import book_ticket
from ticketbooking import search_event, book_ticket

search_event("IPL Final")
book_ticket("IPL Final")
