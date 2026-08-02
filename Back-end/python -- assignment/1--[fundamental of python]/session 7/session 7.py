#1. Skip "Banana" Using continue

fruits = ['Apple', 'Banana', 'Mango', 'Orange']

for fruit in fruits:
    if fruit == 'Banana':
        continue
    print(fruit)
print("**************************************************************")

#2. Stop Search When "Burger King" Is Found Using break

foods = ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King']

for food in foods:
    if food == 'Burger King':
        print('Found Burger King, stopping search.')
        break
    print(food)
print("**************************************************************")

#3. Use pass for the "Focus" Playlist

playlists = ['Chill Vibes', 'Workout', 'Focus', 'Party']

for playlist in playlists:
    if playlist == 'Focus':
        pass
    else:
        print(playlist)
print("**************************************************************")

#4. Filter Spam Messages Using continue and break

messages = ['Hi', 'Spam', 'Hello', 'Spam', 'How are you?']

for message in messages:
    if message == 'Spam':
        continue

    if message == 'How are you?':
        print(message)
        print("Stopping message reading.")
        break

    print(message)
