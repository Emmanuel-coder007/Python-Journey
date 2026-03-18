def double(x):
  return x * 2


double = lambda x: x * 2

print(double(4))
# Output: 8


numbers = [1, 2, 3, 4, 5]

tripled_numbers = list(map(lambda x: x * 3, numbers))

odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))

print(tripled_numbers)  # Output: [3, 6, 9, 12, 15]
print(odd_numbers)      # Output: [1, 3, 5]