#1. insta_caption.py – Print the First 10 Characters


caption = input("Enter your Instagram caption: ")

print("First 10 characters:")
print(caption[:10])
print("************************************************************")

#2. Function extract_artist(song_title)

def extract_artist(song_title):
    dash_position = song_title.index("-")
    artist = song_title[dash_position + 1:].strip()
    return artist

# Example
song = "Shape of You - Ed Sheeran"
print(extract_artist(song))
print("************************************************************")

#3. Function reverse_message(message)

def reverse_message(message):
    reversed_text = ""

    for char in message:
        reversed_text = char + reversed_text

    return reversed_text
print("************************************************************")

#4. Flipkart Product Description Analysis

description = "Samsung Galaxy S25 Ultra 256GB Titanium Black"

words = description.split()

print("First word:", words[0])
print("Last word:", words[-1])
print("Total words:", len(words))
print("************************************************************")

#5. Function mask_phone_number(phone)

def mask_phone_number(phone):
    return "******" + phone[-4:]

