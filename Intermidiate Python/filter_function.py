#Here, we select elements from the data that satisfy the given condition specified by the function and return a new list. It helps extract specific items from a dataset based on the criteria you define. 
#The input function in filter() must return a boolean.


def filter_even(x):
  return x % 2 == 0

even_numbers = filter(filter_even, [1, 2, 3, 4, 5])

print(list(even_numbers)) # Output: [2, 4]

#In this example, the function will go through the list of number and if x % 2 ==0 the function filter_even is true it will print the number.