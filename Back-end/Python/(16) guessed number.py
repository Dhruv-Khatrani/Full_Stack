import random

num=random.randint(1,20)

while True:

    guess=int(input("guessed a number between 1 to 20:"))
    if guess==num:
        print("you guessed a correc number")
        break
    elif guess>num:
        print("you guessed greater number")
    elif guess<num:
        print("you guessed a smailer number")
