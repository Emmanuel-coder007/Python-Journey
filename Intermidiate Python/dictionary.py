# dictionary = {
#     key1: value1,
#     key2: value2,
#     key3: value3
# }

laptop = {
  'brand': 'Apple',
  'model': 'Macbook Pro',
  'size': 14,
  'year': 2023
}

print(laptop['model'])
# Output: Macbook Pro
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creating a dictionary
student_info = {'name': 'Alice', 'age': 9, 'grade': 'A'}

# Accessing dictionary elements
print('Name:', student_info['name'])
print('Age:', student_info['age'])
print('Grade:', student_info['grade'])

# Modifying dictionary elements
student_info['age'] = 10
print('Updated Age:', student_info['age'])

# Dictionary methods
print('Keys:', student_info.keys()) # returns just the keys from a dictionary.
print('Values:', student_info.values()) #returns just the values.
print('Items:', student_info.items()) # returns a list of the key-value pairs as tuples.

#output:
#Keys: dict_keys(['name', 'age', 'grade'])
#Values: dict_values(['Alice', 9, 'A'])
#Items: dict_items([('name', 'Alice'), ('age', 9), ('grade', 'A')])
