from random import sample

famous_houses = [
  '🐺 Stark',
  '🐉 Targaryen',
  '🦌 Baratheon',
  '🦑 Greyjoy',
  '🦁 Lannister'
]

example = sample(famous_houses, 2)

print(f'Example: {example}')

#Since the .sample() method was directly imported,
#  we can just write sample() instead of the usual random.sample().

from random import choice, sample 
#you can import multiple functions 
#from a module in one line by separating them with a comma