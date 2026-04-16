liked_songs = {'Bad Habits': 'Ed Sheeran', 'Shivers': 'Ed Sheeran', 'Ghost': 'Justin Bieber', 'Peaches': 'Justin Bieber', 'Save Your Tears': 'The Weeknd', 'Blinding Lights': 'The Weeknd'}

#Next, create a function to display and write liked songs to a file:
def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as f:
    # handle file here
        f.write('Liked Songs:\n')
        for song, artist in liked_songs.items(): #song is the key, artist is the value
            f.write(f'{song} by {artist}\n')

write_liked_songs_to_file(liked_songs, 'liked_songs.txt')