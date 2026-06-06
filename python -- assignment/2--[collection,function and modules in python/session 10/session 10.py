#1. Create playlist.py

def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist
print("*******************************************************")

#2. Create main.py and Import add_song

from playlist import add_song

playlist = []

add_song("Kesariya", playlist)
add_song("Shape of You", playlist)
add_song("Believer", playlist)

print("Playlist:")
print(playlist)
print("*******************************************************")

#3. Add remove_song() to playlist.py

from playlist import add_song, remove_song

playlist = []

add_song("Kesariya", playlist)
add_song("Shape of You", playlist)
add_song("Believer", playlist)

print("Before Removing:")
print(playlist)

remove_song("Shape of You", playlist)

print("\nAfter Removing:")
print(playlist)
print("*******************************************************")

#4. Add display_playlist() to playlist.py

# main.py

from playlist import add_song, remove_song, display_playlist

playlist = []

# Add songs
add_song("Kesariya", playlist)
add_song("Shape of You", playlist)
add_song("Believer", playlist)

print("After Adding Songs:")
display_playlist(playlist)

# Remove a song
remove_song("Shape of You", playlist)

print("\nAfter Removing 'Shape of You':")
display_playlist(playlist)
