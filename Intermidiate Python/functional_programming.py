import random
import functools

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

random_names = []
def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)


capitalized_suffixes = [suffix.capitalize() for suffix in suffixes]
print('Capitalized Suffixes:', capitalized_suffixes)



def fire_in_name(name):
    while'Fire' in name:
        return True
    return False

def concatenate_names(name1, name2):
    return name1 + ' ' + name2

#Use filter() and apply fire_in_name() to the random_names list.
fire_names = list(filter(fire_in_name, random_names))
#Use reduce() and apply concatenate_names() to the filtered names.

concatenated_fire_names = list(reduce(concatenate_names, fire_names))