#1. Character Frequency Counter

text = input("Enter a string: ")

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
print("*******************************************************")

#2. Word Frequency Counter for a Food Delivery App Review

review = """
Zomato is fast and reliable.
Zomato delivers food quickly.
The food is always fresh!
"""

# Convert to lowercase
review = review.lower()

# Remove punctuation
for ch in ".,!?":
    review = review.replace(ch, "")

words = review.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
print("*******************************************************")

#3. Function word_freq_dict(text)

def word_freq_dict(text):
    text = text.lower()

    for ch in ",.!?":
        text = text.replace(ch, "")

    words = text.split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"

print(word_freq_dict(text))
print("*******************************************************")

#4. Ignore Common Stopwords

def word_freq_dict(text):
    stopwords = ['the', 'and', 'in', 'of', 'a', 'to', 'is']

    text = text.lower()

    for ch in ",.!?":
        text = text.replace(ch, "")

    words = text.split()

    freq = {}

    for word in words:
        if word not in stopwords:
            freq[word] = freq.get(word, 0) + 1

    return freq


text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"

print(word_freq_dict(text))
print("*******************************************************")

#5. Function char_count_dict(text) and Sort by Character

def char_count_dict(text):
    freq = {}

    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


text = input("Enter text: ")

result = char_count_dict(text)

# Print dictionary sorted by character
for char in sorted(result):
    print(char, ":", result[char])
