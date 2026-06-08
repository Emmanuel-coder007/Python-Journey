#Note: Unlike the previous two functions, we must import reduce() from the functools module.

#reduce() takes a collection of iterable data and combines its elements into a single value via a function. An optional initial value can be used, as well.

#This function is ideal for tasks like summing up a list of numbers.

from functools import reduce

def multiply(x, y):
  return x * y
 
product = reduce(multiply, [1, 2, 3, 4, 5])

print(product) # Output: 120