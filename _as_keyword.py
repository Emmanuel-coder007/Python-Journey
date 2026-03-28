import random as rd
# Here, we are renaming the random module with a shorthand, rd.
# From this point of the program, the random module will be known as rd.

# The from and as keywords can also be combined:
from random import sample as samp

example = samp(['Stark', 'Targaryen', 'Baratheon', 'Greyjoy', 'Lannister'], 2)

print('Example: ' + example[0] + ' ' + example[1])
# Instead of typing sample(), we can use the alias we assigned it to, samp().