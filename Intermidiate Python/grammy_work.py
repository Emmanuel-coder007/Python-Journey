from functools import reduce
# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

duration = playlist[0][1] # Get the duration of the first song in the playlist
print (f" {duration}")

def longer_than_five_minutes(song):
    return song[1] > 5.00

final = filter(longer_than_five_minutes, playlist)

durations = [song[1] for song in final] #durations is a list
# for song in final:
    #print(durations.append(song[1]))
print(durations)

def convert_to_seconds(x):
    return playlist[x][1] * 60
 
def add_durations(x, y):
    return x + y

minutes = int(duration)
seconds = (duration - minutes) * 100

total_seconds = minutes * 60 + round(seconds)