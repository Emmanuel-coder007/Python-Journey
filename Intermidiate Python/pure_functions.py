import math

def impure_squared(number):
  result = number ** 2
  print('The square of', number, 'is', result)
  return result

def pure_squared(number):
  return number ** 2

#Pay attention to the syntax:

#The pure function only returns the squared value of number.
#The impure function prints something to the terminal (the side effect).


#area of a circle
def area_of_circle(radius):
  return math.pi * (radius ** 2)

print(area_of_circle(5))