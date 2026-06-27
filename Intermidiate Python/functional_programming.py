import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']


capitalize_suffix = lambda name: name.capitalize()

new_suffixes = list(map(capitalize_suffix, suffixes))



fire_in_name =lambda name: True if 'Fire' in name else False

def concatenate_names(name1, name2):
    return name1 + ', ' + name2

def create_fantasy_name(new_suffixes, prefixes):
  return random.choice(prefixes) + ' ' + random.choice(new_suffixes)

random_names = list(create_fantasy_name(new_suffixes, prefixes) for _ in range(10))

#Use filter() and apply fire_in_name() to the random_names list.
filtered_names = list(filter(fire_in_name, random_names))
#Use reduce() and apply concatenate_names() to the filtered names.

concatenated_fire_names = reduce(concatenate_names, filtered_names)

def display_name_info():
   for name in random_names:
      print(name)
    
   print()
   print('Filtered names: ', filtered_names)
   print('Concatenated names:', concatenated_fire_names)
   
    
display_name_info()


#-------------------------------------------------------------------------------------------------------------------
