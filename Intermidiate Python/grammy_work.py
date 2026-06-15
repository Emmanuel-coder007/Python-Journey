from functools import reduce

playlist = [
    ('What Was I Made For?', 3.42),
    ('Just Like That', 5.05),
    ('Song 3', 6.55),
    ('Leave The Door Open', 4.02),
    ("I Can't Breath", 4.47),
    ('Bad Guy', 3.14)
]

# Helper functions
def longer_than_five_minutes(song):
    return song[1] > 5.00

def minutes_to_seconds(song):
    duration = song[1]
    minutes = int(duration)
    seconds = (duration - minutes) * 100
  
    return minutes * 60 + round(seconds)

def add_durations(total, song):
    return total + song[1]

# Step 1: filter
long_songs = list(filter(longer_than_five_minutes, playlist))

# Step 2: map
songs_in_seconds = list(map(minutes_to_seconds, playlist))

# Step 3: reduce
total_playtime = reduce(add_durations, playlist, 0)

print("Songs longer than 5 mins:", long_songs)
print("Durations in seconds:", songs_in_seconds)
print("Total playtime (mins):", total_playtime)