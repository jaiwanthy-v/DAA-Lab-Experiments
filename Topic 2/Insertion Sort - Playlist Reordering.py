def insert_song(playlist, song):
    i = len(playlist) - 1
    playlist.append(song)

    while i >= 0 and playlist[i][1] > song[1]:
        playlist[i + 1] = playlist[i]
        i -= 1

    playlist[i + 1] = song

    return playlist


playlist = [
    ("Intro", 120),
    ("Chill Beat", 210),
    ("Long Jam", 340)
]

result = insert_song(playlist, ("Quick Track", 180))

print("Sorted Playlist:")

for song in result:
    print(song)
