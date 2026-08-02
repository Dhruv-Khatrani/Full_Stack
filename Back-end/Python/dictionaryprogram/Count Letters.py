text = input("Enter word: ")
d = {}

for ch in text:
    d[ch] = d.get(ch, 0) + 1

print(d)
