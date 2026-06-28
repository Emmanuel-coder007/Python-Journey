

def reverse_string(s):
  return s[::-1]

def capitalize_string(s):
  return s.capitalize()

def is_capitalized(s):
  return s[0].isupper()

print(capitalize_string("hello"))  # Output: "Hello"
print(reverse_string("hello"))      # Output: "olleh"
print(is_capitalized("Hello"))     # Output: True
print(is_capitalized("hello"))     # Output: False