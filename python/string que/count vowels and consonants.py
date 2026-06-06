# given string
s = "hello world"

vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():  # check only letters
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

