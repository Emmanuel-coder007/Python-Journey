def divide_by_2(x):
  return x / 2

halved_numbers = map(divide_by_2, [1, 2, 3, 4, 5])

print(list(halved_numbers))
# Output: [0.5, 1.0, 1.5, 2.0, 2.5]

#map() applies the given function to each element in the data and returns a new list. 
#It's perfect for when you need to perform the same operation on every item in a list, tuple, or data set.