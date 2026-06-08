from functools import reduce
# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

duration = playlist[1]
minutes = int(duration)
seconds = (duration - minutes) * 100

total_seconds = minutes * 60 + round(seconds)

def longer_than_five_minutes(song):
    return song[1] > 5.00

def convert_to_seconds(song):
    return song * 60

def add_durations(x, y):
    return x + y

